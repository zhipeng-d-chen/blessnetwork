import requests
from colorama import Fore
import json
import time
from datetime import datetime, timezone

API_BASE_URL = "https://gateway-run.bls.dev/api/v1"
IP_SERVICE_URL = "https://tight-block-2413.txlabs.workers.dev"

# 读取 'id.txt' 文件的函数
def read_node_and_hardware_id():
    with open("id.txt", "r") as file:
        data = file.read().strip()
        node_id, hardware_id = data.split(":")
        return node_id, hardware_id

# 读取 'user.txt' 文件的函数
def read_auth_token():
    with open("user.txt", "r") as file:
        return file.read().strip()

# 获取外部服务的 IP 地址函数
def fetch_ip_address():
    response = requests.get(IP_SERVICE_URL)
    response.raise_for_status()
    data = response.json()
    print(f"[{datetime.now(timezone.utc).isoformat()}] 获取 IP 响应:", data)
    return data["ip"]

# 注册节点的函数
def register_node(node_id, hardware_id):
    auth_token = read_auth_token()
    register_url = f"{API_BASE_URL}/nodes/{node_id}"
    ip_address = fetch_ip_address()
    print(f"[{datetime.now(timezone.utc).isoformat()}] 正在注册节点，IP: {ip_address}, 硬件 ID: {hardware_id}")
    
    payload = {"ipAddress": ip_address, "hardwareId": hardware_id}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    
    response = requests.post(register_url, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    print(f"[{datetime.now(timezone.utc).isoformat()}] 注册响应:", data)
    return data

# 启动会话的函数
def start_session(node_id):
    auth_token = read_auth_token()
    start_session_url = f"{API_BASE_URL}/nodes/{node_id}/start-session"
    print(f"[{datetime.now(timezone.utc).isoformat()}] 正在启动节点 {node_id} 的会话，可能需要一段时间...")
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(start_session_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(f"[{datetime.now(timezone.utc).isoformat()}] 启动会话响应:", data)
    return data

# 停止会话的函数
def stop_session(node_id):
    auth_token = read_auth_token()
    stop_session_url = f"{API_BASE_URL}/nodes/{node_id}/stop-session"
    print(f"[{datetime.now(timezone.utc).isoformat()}] 正在停止节点 {node_id} 的会话")
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(stop_session_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(f"[{datetime.now(timezone.utc).isoformat()}] 停止会话响应:", data)
    return data

# Ping 节点的函数
def ping_node(node_id):
    auth_token = read_auth_token()
    ping_url = f"{API_BASE_URL}/nodes/{node_id}/ping"
    print(f"[{datetime.now(timezone.utc).isoformat()}] 正在 Ping 节点 {node_id}")
    
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.post(ping_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    last_ping = data["pings"][-1]["timestamp"]
    log_message = (f"[{datetime.now(timezone.utc).isoformat()}] Ping 响应, "
                   f"ID: {data['_id']}, 节点 ID: {data['nodeId']}, 最后 Ping 时间: {last_ping}")
    print(log_message)
    return data

# 显示标题
def display_header():
    custom_ascii_art = f"""
    
               ╔═╗╔═╦╗─╔╦═══╦═══╦═══╦═══╗
               ╚╗╚╝╔╣║─║║╔══╣╔═╗║╔═╗║╔═╗║
               ─╚╗╔╝║║─║║╚══╣║─╚╣║─║║║─║║
               ─╔╝╚╗║║─║║╔══╣║╔═╣╚═╝║║─║║
               ╔╝╔╗╚╣╚═╝║╚══╣╚╩═║╔═╗║╚═╝║
               ╚═╝╚═╩═══╩═══╩═══╩╝─╚╩═══╝
    """
    
    print(custom_ascii_art)
    print(f"{Fore.YELLOW}我的gihub：github.com/Gzgod")
    print("我的推特：推特雪糕战神@Hy78516012  ")
    print("TG群：https://t.me/+FZHZVA_gEOJhOWM1  ")
    print("TG群（土狗交流）：https://t.me/+0X5At4YG0_k0ZThl  ")
    print(f"\n")
    

# 主函数
def run_all():
    try:
        display_header()
        node_id, hardware_id = read_node_and_hardware_id()
        print(f"[{datetime.now(timezone.utc).isoformat()}] 读取到的节点 ID: {node_id}, 硬件 ID: {hardware_id}")
        
        registration_response = register_node(node_id, hardware_id)
        print(f"[{datetime.now(timezone.utc).isoformat()}] 节点注册完成。响应:", registration_response)
        
        start_session_response = start_session(node_id)
        print(f"[{datetime.now(timezone.utc).isoformat()}] 会话已启动。响应:", start_session_response)
        
        print(f"[{datetime.now(timezone.utc).isoformat()}] 发送初始 Ping...")
        ping_node(node_id)
        
        while True:
            print(f"[{datetime.now(timezone.utc).isoformat()}] 发送 Ping...")
            ping_node(node_id)
            time.sleep(60)
    
    except Exception as error:
        print(f"[{datetime.now(timezone.utc).isoformat()}] 发生错误:", error)

if __name__ == "__main__":
    run_all()

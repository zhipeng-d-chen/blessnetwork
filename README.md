#### 注册 Bless Network
[https://bless.network/dashboard?ref=UKVXVH](https://bless.network/dashboard?ref=UKVXVH)

#### 功能
- 自动化节点交互

#### 加入我的 Telegram 频道
   ```sh
   TG撸毛群：https://t.me/+FZHZVA_gEOJhOWM1
   ```
   ```sh
   TG土狗群：https://t.me/+0X5At4YG0_k0ZThl
   ```
#### 安装
1. 将仓库克隆到本地机器：
   ```sh
   git clone https://github.com/Gzgod/blessnetwork.git
   ```
2. 进入项目目录：
   ```sh
   cd blessnetwork
   ```
3. 安装必要的依赖：
   ```sh
   pip install -r requirements.txt
   ```
4. 运行脚本：
   ```sh
   python3 main.py
   ```

#### 使用
1. 首先注册 Blockless Bless Network 账户，如果没有请在此注册：[注册链接](https://bless.network/dashboard?ref=UKVXVH)
2. 设置并修改 `user.txt`。将您的 B7S_AUTH_TOKEN 放入文本文件中，示例如下：
   ```
   eyJhbGcixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```
   获取令牌的方法如下：
   - 登录到 [Bless Network 仪表盘](https://bless.network/dashboard?ref=UKVXVH)，确保在此链接下进行下一步操作。
   - 打开开发者工具，按 F12 或右键单击浏览器中的检查元素。
   - 转到console标签并粘贴以下内容：
     ```js
     localStorage.getItem('B7S_AUTH_TOKEN')
     ```

3. 设置并修改 `id.txt`。将您的节点 ID（pubkey）和硬件 ID 按以下格式放入文本文件中，示例如下：
   ```
   12D3Koxxxxxxxxxxxxxxx:e938610xxxxxxxxxxxx
   ```
   获取节点 ID 和硬件 ID 的方法如下：
   - 下载扩展程序。
   - 下载后，打开 `chrome://extensions/?id=pljbjcehnhcnofmkdbjolghdcjnmekia`。
   - 在右上角启用开发者模式，然后按服务工作者。您将看到一个新标签页打开。
   - ![image](https://github.com/user-attachments/assets/5b383794-dabc-46f8-9bd2-0ded4453afe3)
   - 转到网络标签，然后打开 Bless 扩展程序并登录您的账户。
   - ![image](https://github.com/user-attachments/assets/72a55655-c8c7-43a5-9dc4-a0f824b1ad5e)
   - 登录后，搜索带有您的 pubkey 的名称（例如：12D3xxxx），打开并复制 pubkey 和硬件 ID。
   - <img width="747" alt="75f07d433d27a5941dfd3ac4057999b" src="https://github.com/user-attachments/assets/c090c37c-ea85-4d63-bdd5-ab8ac74a9322">
4. 运行脚本：
   ```sh
   python3 bot.py
   ```

#### 注意
- 总时间每 10 分钟刷新一次连接。
- 每个账户最多只能有 5 个节点 ID，且不能删除。建议保存您的节点 ID（pubkey）和硬件 ID。

# AzurPilot 安装与使用指南

## 系统要求

| 项目 | 要求 |
|------|------|
| Python | >=3.14, <3.15 |
| 包管理器 | [uv](https://docs.astral.sh/uv/) |
| ADB | [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools) |
| 模拟器 | 夜神 / 雷电 / 蓝叠 / MuMu12（支持 ADB） |
| 分辨率 | 1280x720，平板模式 |
| 磁盘 | 约 1.5 GB 可用空间 |

---

## 一、安装 AzurPilot

### 1. 安装 uv（包管理器）

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

验证安装：`uv --version`

### 2. 克隆仓库

```bash
git clone https://github.com/wess09/AzurPilot.git
cd AzurPilot
```

### 3. 安装依赖

```bash
uv sync --frozen
```

此命令会自动创建 `.venv` 虚拟环境并安装 pyproject.toml 中声明的全部 50+ 个依赖。安装完成后所有命令都需要在项目根目录执行。

### 4. 安装 ADB

下载 [Android Platform Tools](https://developer.android.com/studio/releases/platform-tools)，将 `adb` 放入系统 PATH。

验证安装：`adb devices`

### 5. 替换模拟器 ADB（国产模拟器必需）

国产模拟器（夜神、雷电、蓝叠、MuMu）使用自带的旧版 ADB，会和最新版 ADB 互相冲突导致断连。

```
模拟器安装目录/
├── adb.exe        # 替换
└── nox_adb.exe    # 重命名（如夜神）
```

找到模拟器安装目录下的 `adb.exe`，备份后替换为下载的 Platform Tools 中的 `adb.exe`。如果有多个 ADB 文件（如夜神的 `adb.exe` 和 `nox_adb.exe`），全部替换。

替换后重启模拟器，验证：`adb devices` 应看到设备列表。

### 6. 安装 uiautomator2

打开模拟器，执行：

```bash
uv run python -m uiautomator2 init
```

模拟器中会出现一个名为 `ATX` 的小黄车图标，表示安装成功。

---

## 二、模拟器与游戏设置

### 模拟器设置

| 设置 | 值 |
|------|-----|
| 分辨率 | 1280x720 |
| 显示类型 | 平板模式 |
| ADB | 开启（蓝叠/雷电需手动开启） |
| 手机 GUI 保活 | 关闭（MuMu12） |

### 游戏内设置

路径：主界面 -> 右下角设置 -> 左侧边栏

| 设置 | 值 |
|------|-----|
| 帧数设置 | 60 帧 |
| 大型作战，减少 TB 引导 | 开 |
| 大型作战，自律时自动提交道具 | 开 |
| 大型作战，安全海域默认开启自律 | 关 |
| 剧情自动播放 | 开启 |
| 剧情自动播放速度调整 | 特快 |
| 待机模式设置，启用待机模式 | 关 |
| 重复角色获得提示 | 关 |
| 快速更换二次确认界面 | 关 |
| 展示结算角色 | 关 |

路径：大型作战 -> 右上角雷达 -> 指令模块 -> 潜艇支援

| 设置 | 值 |
|------|-----|
| X 消耗时潜艇出击 | 取消勾选 |

路径：主界面 -> 建造 -> 退役 -> 一键退役设置

| 设置 | 值 |
|------|-----|
| 选择优先级 1 | R |
| 选择优先级 2 | SR |
| 选择优先级 3 | N |

---

## 三、启动与配置

### 启动 AzurPilot

**方式一：一键启动（推荐）**

Windows 双击 `run.bat`，或在命令行执行：

```bash
python launcher.py
```

启动器会自动打开 WebUI 并在浏览器中访问。

**方式二：手动启动 WebUI**

```bash
uv run python gui.py
```

然后在浏览器打开 `http://127.0.0.1:25548`。

### 首次配置（OOBE）

首次打开 WebUI 会自动进入设置向导：

1. 选择语言（中文 / English）
2. 选择游戏服务器（CN / EN / JP / TW）
3. 填写模拟器 Serial（如 `127.0.0.1:5555` 或 `emulator-5554`）
4. 选择游戏客户端（服务器对应包名）

### 手动配置

WebUI 中进入 Alas 设置：

| 配置项 | 说明 |
|--------|------|
| 模拟器 Serial | ADB 设备序列号，`adb devices` 查看 |
| 游戏客户端 | 服务器对应的包名，自动识别可留空 |
| 游戏内服务器 | 你的游戏区服名称 |
| 模拟器设置 | 截图方案、点击方案 |

### 运行性能测试

1. WebUI 侧边栏选择「性能测试」（需要主线推到第 7 章）
2. 点击「运行」，等待测试结束
3. 记录最快的截图方案和点击方案（截图+点击 < 350ms 为佳）
4. 在 Alas 设置 -> 模拟器设置 中应用最快的方案

---

## 四、使用 AzurPilot

### 启用任务

1. WebUI 侧边栏选择要运行的任务（科研、委托、战术学院、每日、战役等）
2. 打开任务开关（Enable）
3. 根据需要修改任务参数
4. 支持同时启用多个任务，AzurPilot 会自动调度

### 开始运行

1. 侧边栏选择「总览」
2. 确认任务队列中显示已启用的任务
3. 点击「开始」启动调度器

### 查看状态

| 页面 | 功能 |
|------|------|
| 总览 | 任务队列、运行状态、资源概览 |
| 仪表盘 | AP 图表、金币/紫币走势、虚拟资产 |
| 日志 | 实时运行日志 |
| 性能测试 | 截图/点击方案基准测试 |

### 停止运行

点击「停止」按钮，调度器会在当前任务完成后停止。

---

## 五、MCP 服务（AI 远程管理）

### 启动 MCP 服务

```bash
uv run python mcp_server_sse.py
```

默认端口 22268。

### 客户端配置

支持 MCP 的客户端（如 Claude Code、Cursor）通过 SSE 连接：

```json
{
  "mcpServers": {
    "alas": {
      "url": "http://127.0.0.1:22267/mcp/sse"
    }
  }
}
```

云端部署替换 `127.0.0.1` 为服务器 IP。

### 可用工具

| 类别 | 工具 |
|------|------|
| 实例管理 | list_instances、get_status、start_instance、stop_instance |
| 任务管理 | list_tasks、get_task_help、trigger_task、get_scheduler_queue、clear_scheduler_queue |
| 监控 | get_current_running_task、get_resources、get_config、get_recent_logs、get_screenshot |
| 配置 | update_config |
| 维护 | restart_emulator、restart_adb、update_alas |

---

## 六、常见问题

### uv sync 失败

```bash
# 国内用户设置镜像源
export UV_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
uv sync --frozen
```

### ADB 连接断开

```bash
adb kill-server
adb start-server
adb devices
```

### ATX 小黄车消失

重新执行：`uv run python -m uiautomator2 init`

### WebUI 白屏

按 `CTRL+R` 刷新页面，或重启 gui.py。

### 任务连续失败

WebUI 日志页面查看具体错误，常见原因：
- 模拟器分辨率不是 1280x720
- 游戏内设置未按要求修改
- ADB 版本冲突导致截图超时

---

## 七、更新

```bash
cd AzurPilot
git pull
uv sync --frozen
```

如果使用 WebUI，启动时自动检查更新（可在 `config/deploy.yaml` 中关闭）。
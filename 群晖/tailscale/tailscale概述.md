# tailscale
## OverView

可能会选择使用 frp 等针对特定协议和端口的内网穿透方案，但这种方案还是不够酸爽，无法访问家庭内网任意设备的任意端口。更佳的选择还是通过 VPN 来组建大内网。至于该选择哪种 VPN，毫无疑问肯定是 WireGuard，WireGuard 就是 VPN 的未来。**我已经不止一次向大家推荐使用 WireGuard 了，我累了，不想再讲了，你爱 JB 用辣鸡 OpenVPN 之类的就用吧，你开心就好。**

# WireGuard
比传统VPN的核心优势是没有VPN网关，所有节点之间都可以点对点 P2P 连接，也就是全互联模式（full mesh) ，效率更高，速度更快，成本更低

WireGuard 目前最大的痛点就是上层应用的功能不够健全，因为 WireGuard 推崇的是 Unix 的哲学，WireGuard 本身只是一个内核级别的模块，只是一个数据平面，至于上层的更高级的功能（比如秘钥交换机制，UDP 打洞，ACL 等），需要通过用户空间的应用来实现。

## Netmaker
它通过可视化界面来配置 WireGuard 的全互联模式，它支持 UDP 打洞、多租户等各种高端功能，几乎适配所有平台，非常强大。然而现实世界是复杂的，无法保证所有的 NAT 都能打洞成功，且 Netmaker 目前还没有 fallback 机制，如果打洞失败，无法 fallback 改成走中继节点。


## tailscale
Tailscale 在这一点上比 Netmaker 高明许多，它支持 fallback 机制，可以尽最大努力实现全互联模式，部分节点即使打洞不成功，也能通过中继节点在这个虚拟网络中畅通无阻。

### 是什么
Tailscale 是一种基于 WireGuard 的虚拟组网工具，和 Netmaker 类似，**最大的区别在于 Tailscale 是在用户态实现了 WireGuard 协议，而 Netmaker 直接使用了内核态的 WireGuard**。所以 Tailscale 相比于内核态 WireGuard 性能会有所损失，但与 OpenVPN 之流相比还是能甩好几十条街的，Tailscale 虽然在性能上做了些许取舍，但在功能和易用性上绝对是完爆其他工具：

- 开箱即用
    - 无需配置防火墙
    - 没有额外的配置
- 高安全性/私密性
    - 自动密钥轮换
    - 点对点连接
    - 支持用户审查端到端的访问记录
- 在原有的 ICE、STUN 等 UDP 协议外，实现了 DERP TCP 协议来实现 NAT 穿透
- 基于公网的控制服务器下发 ACL 和配置，实现节点动态更新
- 通过第三方（如 Google） SSO 服务生成用户和私钥，实现身份认证

简而言之，我们可以将 Tailscale 看成是更为易用、功能更完善的 WireGuard。

![图片描述: 2022-03-20-14-50-Q4bWmK.png](https://images.icloudnative.io/uPic/2022-03-20-14-50-Q4bWmK.png)

光有这些还不够，作为一个白嫖党，咱更关心的是**免费**与**开源**。

Tailscale 是一款商业产品，但个人用户是可以白嫖的，个人用户在接入设备不超过 20 台的情况下是可以免费使用的（虽然有一些限制，比如子网网段无法自定义，且无法设置多个子网）。除 Windows 和 macOS 的图形应用程序外，其他 Tailscale 客户端的组件（包含 Android 客户端）是在 BSD 许可下以开源项目的形式开发的，你可以在他们的 [GitHub 仓库](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL3RhaWxzY2FsZS8%3d)找到各个操作系统的客户端源码。

对于大部份用户来说，白嫖 Tailscale 已经足够了，如果你有更高的需求，比如自定义网段，可以选择付费。

**我就不想付费行不行？行，不过得往下看。**

## Headscale 是什么

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#headscale-%E6%98%AF%E4%BB%80%E4%B9%88)

Tailscale 的控制服务器是不开源的，而且对免费用户有诸多限制，这是人家的摇钱树，可以理解。好在目前有一款开源的实现叫 [Headscale](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL2p1YW5mb250L2hlYWRzY2FsZQ%3d%3d)，这也是唯一的一款，希望能发展壮大。

Headscale 由欧洲航天局的 Juan Font 使用 Go 语言开发，在 BSD 许可下发布，实现了 Tailscale 控制服务器的所有主要功能，可以部署在企业内部，没有任何设备数量的限制，且所有的网络流量都由自己控制。

## Headscale 部署

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#headscale-%E9%83%A8%E7%BD%B2)

### 使用 Sealos 一键部署

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E4%BD%BF%E7%94%A8-sealos-%E4%B8%80%E9%94%AE%E9%83%A8%E7%BD%B2)

如果你嫌下面太长不看，可以选择直接使用 Sealos 应用模板一键部署，有手就行，啥都不需要设置。

直接点击下面的按钮跳转到 Sealos 的应用模板部署界面：

[![图片描述: Deploy-on-Sealos.svg](https://cdn.jsdelivr.net/gh/labring-actions/templates@main/Deploy-on-Sealos.svg)](https://bja.sealos.run/?openapp=system-template%3FtemplateName%3Dheadscale)

> 如果您是第一次打开 [Sealos](https://icloudnative.io/go/?target=aHR0cHM6Ly9zZWFsb3MucnVu)，需要先注册登录账号。

然后点击「部署应用」按钮开始部署。部署完成后，你会看到两个应用，一个是 Headscale，另一个则是 [Headscale 可视化界面](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL0dvb2RpZXNIUS9oZWFkc2NhbGUtYWRtaW4%3d)。

![图片描述: 2024-01-07-17-35-ceoOvP.png](https://images.icloudnative.io/uPic/2024-01-07-17-35-ceoOvP.png)

点击 Headscale 应用的「详情」进入详情页面。内网端口 8080 对应的外网地址就是 Headscale 的公网域名。

![图片描述: 2024-01-07-17-38-HL3z2X.png](https://images.icloudnative.io/uPic/2024-01-07-17-38-HL3z2X.png)

Headscale 公网域名后面跟上路径 `/admin/` 即可打开可视化界面。

![图片描述: 2024-01-07-17-39-42E6NM.jpg](https://images.icloudnative.io/uPic/2024-01-07-17-39-42E6NM.jpg)

### 在 Linux 上部署

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E5%9C%A8-linux-%E4%B8%8A%E9%83%A8%E7%BD%B2)

Headscale 部署很简单，推荐直接在 Linux 主机上安装。

> 理论上来说只要你的 Headscale 服务可以暴露到公网出口就行，但最好不要有 NAT，所以推荐将 Headscale 部署在有公网 IP 的云主机上。

首先需要到其 GitHub 仓库的 Release 页面下载最新版的二进制文件。

```bash
$ wget --output-document=/usr/local/bin/headscale \
   https://github.com/juanfont/headscale/releases/download/v<HEADSCALE VERSION>/headscale_<HEADSCALE VERSION>_linux_<ARCH>

$ chmod +x /usr/local/bin/headscale
```

创建配置目录：

```bash
$ mkdir -p /etc/headscale
```

创建目录用来存储数据与证书：

```bash
$ mkdir -p /var/lib/headscale
```

创建空的 SQLite 数据库文件：

```bash
$ touch /var/lib/headscale/db.sqlite
```

创建 Headscale 配置文件：

```bash
$ wget https://github.com/juanfont/headscale/raw/main/config-example.yaml -O /etc/headscale/config.yaml
```

- 修改配置文件，将 `server_url` 改为公网 IP 或域名。**如果是国内服务器，域名必须要备案**。我的域名无法备案，所以我就直接用公网 IP 了。
- 如果暂时用不到 DNS 功能，可以先将 `magic_dns` 设为 false。
- `server_url` 设置为 `http://<PUBLIC_ENDPOINT>:8080`，将 `<PUBLIC_ENDPOINT>` 替换为公网 IP 或者域名。
- 建议打开随机端口，将 randomize_client_port 设为 true。
- 可自定义私有网段，也可同时开启 IPv4 和 IPv6：
    
    ```yaml
    ip_prefixes:
      # - fd7a:115c:a1e0::/48
      - 100.64.0.0/16
    ```
    

创建 SystemD service 配置文件：

```bash
# /etc/systemd/system/headscale.service
[Unit]
Description=headscale controller
After=syslog.target
After=network.target

[Service]
Type=simple
User=headscale
Group=headscale
ExecStart=/usr/local/bin/headscale serve
Restart=always
RestartSec=5

# Optional security enhancements
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ProtectHome=yes
ReadWritePaths=/var/lib/headscale /var/run/headscale
AmbientCapabilities=CAP_NET_BIND_SERVICE
RuntimeDirectory=headscale

[Install]
WantedBy=multi-user.target
```

创建 headscale 用户：

```bash
$ useradd headscale -d /home/headscale -m
```

修改 /var/lib/headscale 目录的 owner：

```bash
$ chown -R headscale:headscale /var/lib/headscale
```

修改配置文件中的 `unix_socket`：

```yaml
unix_socket: /var/run/headscale/headscale.sock
```

Reload SystemD 以加载新的配置文件：

```bash
$ systemctl daemon-reload
```

启动 Headscale 服务并设置开机自启：

```bash
$ systemctl enable --now headscale
```

查看运行状态：

```bash
$ systemctl status headscale
```

查看占用端口：

```bash
$ ss -tulnp|grep headscale

tcp LISTEN 0 1024 [::]:9090 [::]:* users:(("headscale",pi

d=10899,fd=13))

tcp LISTEN 0 1024 [::]:50443 [::]:* users:(("headscale",pi

d=10899,fd=10))

tcp LISTEN 0 1024 [::]:8080 [::]:* users:(("headscale",pi

d=10899,fd=12))
```

## 创建用户

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E5%88%9B%E5%BB%BA%E7%94%A8%E6%88%B7)

### 命令行

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E5%91%BD%E4%BB%A4%E8%A1%8C)

Tailscale 中有一个概念叫 tailnet，你可以理解成租户，租户与租户之间是相互隔离的，具体看参考 Tailscale 的官方文档： [What is a tailnet](https://icloudnative.io/go/?target=aHR0cHM6Ly90YWlsc2NhbGUuY29tL2tiLzExMzYvdGFpbG5ldC8%3d)。Headscale 也有类似的实现叫 user，即用户。我们需要先创建一个 user，以便后续客户端接入，例如：

```bash
$ headscale user create default
```

查看命名空间：

```bash
$ headscale user list

ID | Name | Created

1 | default | 2022-03-09 06:12:06
```

如果你是通过 Sealos 一键部署的 Headscale，可以在 Headscale 应用的详情页面点击右侧的「终端」按钮进入 Headscale 容器的终端：

![图片描述: 2023-12-29-16-03-EKHluF.png](https://images.icloudnative.io/uPic/2023-12-29-16-03-EKHluF.png)

然后在终端中执行上述命令创建 user。

### 可视化界面

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E5%8F%AF%E8%A7%86%E5%8C%96%E7%95%8C%E9%9D%A2)

[Headscale-Admin](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL0dvb2RpZXNIUS9oZWFkc2NhbGUtYWRtaW4%3d) 需要通过 API Key 来接入 Headscale，所以在使用之前我们需要先创建一个 API key。在 Headscale 应用的详情页面点击右侧的「终端」按钮进入 Headscale 容器的终端：

![图片描述: 2023-12-29-16-03-EKHluF.png](https://images.icloudnative.io/uPic/2023-12-29-16-03-EKHluF.png)

然后执行以下命令创建 API Key：

```bash
$ headscale apikey create
```

将 Headscale 公网域名和 API Key 填入 Headscale-Admin 的设置页面，同时取消勾选 Legacy API，然后点击「Save」：

![图片描述: 2024-01-07-19-05-bF4O80.jpg](https://images.icloudnative.io/uPic/2024-01-07-19-05-bF4O80.jpg)

接入成功后，点击左边侧栏的「Users」，然后点击「Create」开始创建用户：

![图片描述: 2024-01-07-19-24-M1KVMw.jpg](https://images.icloudnative.io/uPic/2024-01-07-19-24-M1KVMw.jpg)

## Tailscale 客户端接入

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#tailscale-%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%8E%A5%E5%85%A5)

目前除了 iOS 客户端，其他平台的客户端都有办法自定义 Tailscale 的控制服务器。

|OS|是否支持 Headscale|
|---|---|
|Linux|Yes|
|OpenBSD|Yes|
|FreeBSD|Yes|
|macOS|Yes|
|Windows|Yes 参考 [Windows 客户端文档](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL2p1YW5mb250L2hlYWRzY2FsZS9ibG9iL21haW4vZG9jcy93aW5kb3dzLWNsaWVudC5tZA%3d%3d)|
|Android|Yes|
|iOS|Yes|

我们先来看下 Linux 平台的接入。

### Linux

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#linux)

Tailscale 官方提供了各种 Linux 发行版的软件包，但国内的网络你懂得，软件源根本用不了。好在官方还提供了 [静态编译的二进制文件](https://icloudnative.io/go/?target=aHR0cHM6Ly90YWlsc2NhbGUuY29tL2Rvd25sb2FkL2xpbnV4L3N0YXRpYw%3d%3d)，我们可以直接下载。例如：

```bash
$ wget https://pkgs.tailscale.com/stable/tailscale_1.22.2_amd64.tgz
```

解压：

```bash
$ tar zxvf tailscale_1.22.2_amd64.tgz
x tailscale_1.22.2_amd64/
x tailscale_1.22.2_amd64/tailscale
x tailscale_1.22.2_amd64/tailscaled
x tailscale_1.22.2_amd64/systemd/
x tailscale_1.22.2_amd64/systemd/tailscaled.defaults
x tailscale_1.22.2_amd64/systemd/tailscaled.service
```

将二进制文件复制到官方软件包默认的路径下：

```bash
$ cp tailscale_1.22.2_amd64/tailscaled /usr/sbin/tailscaled
$ cp tailscale_1.22.2_amd64/tailscale /usr/bin/tailscale
```

将 systemD service 配置文件复制到系统路径下：

```bash
$ cp tailscale_1.22.2_amd64/systemd/tailscaled.service /lib/systemd/system/tailscaled.service
```

将环境变量配置文件复制到系统路径下：

```bash
$ cp tailscale_1.22.2_amd64/systemd/tailscaled.defaults /etc/default/tailscaled
```

启动 tailscaled.service 并设置开机自启：

```bash
$ systemctl enable --now tailscaled
```

查看服务状态：

```bash
$ systemctl status tailscaled
```

Tailscale 接入 Headscale：

```bash
# 如果你是在自己的服务器上部署的，请将 <HEADSCALE_PUB_ENDPOINT> 换成你的 Headscale 公网 IP 或域名
$ tailscale up --login-server=http://<HEADSCALE_PUB_ENDPOINT>:8080 --accept-routes=true --accept-dns=false

# 如果你是使用 Sealos 一键部署的，请将 <HEADSCALE_PUB_ENDPOINT> 换成上文提到的 Sealos 中的 Headscale 公网域名
$ tailscale up --login-server=https://<HEADSCALE_PUB_ENDPOINT> --accept-routes=true --accept-dns=false
```

你也可以在 Headsca-Admin 的 Deploy 界面获取接入命令：

![图片描述: 2024-01-07-19-28-7nsZjl.jpg](https://images.icloudnative.io/uPic/2024-01-07-19-28-7nsZjl.jpg)

这里推荐将 DNS 功能关闭，因为它会覆盖系统的默认 DNS。如果你对 DNS 有需求，可自己研究官方文档，这里不再赘述。

执行完上面的命令后，会出现下面的信息：

```bash
To authenticate, visit:

	https://qgemohpy.cloud.sealos.io/register/mkey:e13651ddbfc269513723f1afd6f42465e56922b67ecea8f37d61a35b1b357e0c
```

在浏览器中打开该链接，就会出现如下的界面：

![图片描述: 2023-12-29-16-23-vrj10n.png](https://images.icloudnative.io/uPic/2023-12-29-16-23-vrj10n.png)

将其中的命令复制粘贴到 headscale 所在机器的终端中，并将 USERNAME 替换为前面所创建的 user。

```bash
$ headscale nodes register --user default --key 905cf165204800247fbd33989dbc22be95c987286c45aac3033937041150d846
Machine register
```

注册成功，查看注册的节点：

```bash
$ headscale nodes list

ID | Name | NodeKey | Namespace | IP addresses | Ephemeral | Last seen | Onlin

e | Expired

1 | coredns | [Ew3RB] | default | 100.64.0.1 | false | 2022-03-20 09:08:58 | onlin

e | no
```

回到 Tailscale 客户端所在的 Linux 主机，可以看到 Tailscale 会自动创建相关的路由表和 iptables 规则。路由表可通过以下命令查看：

```bash
$ ip route show table 52
```

查看 iptables 规则：

```bash
$ iptables -S
-P INPUT DROP
-P FORWARD ACCEPT
-P OUTPUT ACCEPT
-N ts-forward
-N ts-input
-A INPUT -j ts-input
-A FORWARD -j ts-forward
-A ts-forward -i tailscale0 -j MARK --set-xmark 0x40000/0xffffffff
-A ts-forward -m mark --mark 0x40000 -j ACCEPT
-A ts-forward -s 100.64.0.0/10 -o tailscale0 -j DROP
-A ts-forward -o tailscale0 -j ACCEPT
-A ts-input -s 100.64.0.5/32 -i lo -j ACCEPT
-A ts-input -s 100.115.92.0/23 ! -i tailscale0 -j RETURN
-A ts-input -s 100.64.0.0/10 ! -i tailscale0 -j DROP

$ iptables -S -t nat
-P PREROUTING ACCEPT
-P INPUT ACCEPT
-P OUTPUT ACCEPT
-P POSTROUTING ACCEPT
-A ts-postrouting -m mark --mark 0x40000 -j MASQUERADE
```

### macOS

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#macos)

macOS 有 3 种安装方法：

- 直接通过应用商店安装，地址： [https://apps.apple.com/ca/app/tailscale/id1475387142](https://icloudnative.io/go/?target=aHR0cHM6Ly9hcHBzLmFwcGxlLmNvbS9jYS9hcHAvdGFpbHNjYWxlL2lkMTQ3NTM4NzE0Mg%3d%3d)。前提是你**需要一个美区 ID**。。。
- 下载 [安装包](https://icloudnative.io/go/?target=aHR0cHM6Ly9wa2dzLnRhaWxzY2FsZS5jb20vc3RhYmxlLyNtYWNvcw%3d%3d)直接安装，绕过应用商店。
- 安装开源的命令行工具 `tailscale` 和 `tailscaled`。相关链接： [https://github.com/tailscale/tailscale/wiki/Tailscaled-on-macOS](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL3RhaWxzY2FsZS90YWlsc2NhbGUvd2lraS9UYWlsc2NhbGVkLW9uLW1hY09T)。

这三种安装包的核心数据包处理代码是相同的，唯一的区别在于在于打包方式以及与系统的交互方式。

应用商店里的应用运行在一个 [应用沙箱](https://icloudnative.io/go/?target=aHR0cHM6Ly9kZXZlbG9wZXIuYXBwbGUuY29tL2xpYnJhcnkvYXJjaGl2ZS9kb2N1bWVudGF0aW9uL1NlY3VyaXR5L0NvbmNlcHR1YWwvQXBwU2FuZGJveERlc2lnbkd1aWRlL0Fib3V0QXBwU2FuZGJveC9BYm91dEFwcFNhbmRib3guaHRtbA%3d%3d)中，与系统的其他部分隔离。在沙箱内，应用可以是一个 [网络扩展](https://icloudnative.io/go/?target=aHR0cHM6Ly9kZXZlbG9wZXIuYXBwbGUuY29tL2RvY3VtZW50YXRpb24vbmV0d29ya2V4dGVuc2lvbg%3d%3d)，以实现 VPN 或者类 VPN 的功能。网络扩展实现的功能对应用商店之外的应用是无法生效的。

从 macOS 从 10.15 开始新增了 [系统扩展](https://icloudnative.io/go/?target=aHR0cHM6Ly9kZXZlbG9wZXIuYXBwbGUuY29tL3N5c3RlbS1leHRlbnNpb25zLw%3d%3d)，说白了就是运行在用户态的内核扩展，它相比于传统的网络扩展增强了很多功能，比如内容过滤、透明代理、DNS 代理等。Tailscale 独立于应用商店的安装包使用的就是**系统扩展**，通过 DMG 或者 zip 压缩包进行分发。

不要同时安装应用商店版本和独立分发版本，同时只能装一个。

而命令行工具既没有使用网络扩展也没有使用系统扩展，而是使用的 [utun 接口](https://icloudnative.io/go/?target=aHR0cHM6Ly9lbi53aWtpcGVkaWEub3JnL3dpa2kvVFVOL1RBUA%3d%3d)，相比于 GUI 版本缺少了部分功能，比如 MagicDNS 和 Taildrop。

总览：

||应用商店（网络扩展）|独立应用（系统扩展）|命令行版本|
|---|---|---|---|
|是否可用|[yes](https://icloudnative.io/go/?target=aHR0cHM6Ly9hcHBzLmFwcGxlLmNvbS9jYS9hcHAvdGFpbHNjYWxlL2lkMTQ3NTM4NzE0Mg%3d%3d)|yes, [beta](https://icloudnative.io/go/?target=aHR0cHM6Ly90YWlsc2NhbGUuY29tL2tiLzExNjcvcmVsZWFzZS1zdGFnZXMvI2JldGE%3d)|[yes](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL3RhaWxzY2FsZS90YWlsc2NhbGUvd2lraS9UYWlsc2NhbGVkLW9uLW1hY09T)|
|图形界面|yes|yes|no; CLI|
|macOS 最低版本|macOS 10.13|macOS 10.15|macOS 10.13|
|后台运行|no; sandboxed|理论上支持; 尚未实现|yes|
|使用的钥匙串🔑|用户级|系统级|直接存放在文件中|
|沙盒隔离|yes|no|no|
|自动更新|yes; 应用商店直接更新|yes; [Sparkle](https://icloudnative.io/go/?target=aHR0cHM6Ly9zcGFya2xlLXByb2plY3Qub3JnLw%3d%3d)|no|
|是否开源|no|no|yes|
|MagicDNS|yes|yes|yes|
|Taildrop|yes|yes|未实现|

安装完 GUI 版应用后还需要做一些骚操作，才能让 Tailscale 使用 Headscale 作为控制服务器。当然，Headscale 已经给我们提供了详细的操作步骤，你只需要在浏览器中打开 URL：`https://<HEADSCALE_PUB_ENDPOINT>/apple`，便会出现如下的界面：

![图片描述: 2023-12-29-16-50-lgDjCB.png](https://images.icloudnative.io/uPic/2023-12-29-16-50-lgDjCB.png)

对于 1.34.0 及以上的 Tailscale 版本，可以按照下面的方法来操作：

1. 长按「ALT」键，然后点击顶部菜单栏的 Tailscale 图标，然后将鼠标指针悬停在「Debug」菜单上。
    
    ![图片描述: 2023-12-29-17-04-fPLtsa.png](https://images.icloudnative.io/uPic/2023-12-29-17-04-fPLtsa.png)
    
2. 在「Custom Login Server」下方选择「Add Account…」。
    
3. 在打开的弹窗中填入 Headscale 的公网域名，然后点击「Add Account」。
    
    ![图片描述: 2023-12-29-17-13-0LVi0S.png](https://images.icloudnative.io/uPic/2023-12-29-17-13-0LVi0S.png)
    
4. 然后立马就会跳转到浏览器并打开一个页面。
    
    ![图片描述: 2023-12-29-17-14-3VPcX4.png](https://images.icloudnative.io/uPic/2023-12-29-17-14-3VPcX4.png)
    
5. 接下来与之前 Linux 客户端相同，回到 Headscale 所在的机器执行浏览器中的命令即可，注册成功：
    
    ![图片描述: 2022-03-20-17-51-Gcjcmy.png](https://images.icloudnative.io/uPic/2022-03-20-17-51-Gcjcmy.png)
    

回到 Headscale 所在主机，查看注册的节点：

```bash
$ headscale nodes list

ID | Name | NodeKey | Namespace | IP addresses | Ephemeral | Last seen | Onlin

e | Expired

1 | coredns | [Ew3RB] | default | 100.64.0.1 | false | 2022-03-20 09:08:58 | onlin

e | no
2 | carsondemacbook-pro | [k7bzX] | default   | 100.64.0.2     | false     | 2022-03-20 09:48:30 | online  | no
```

回到 macOS，测试是否能 ping 通对端节点：

```bash
$ ping -c 2 100.64.0.1
PING 100.64.0.1 (100.64.0.1): 56 data bytes
64 bytes from 100.64.0.1: icmp_seq=0 ttl=64 time=37.025 ms
64 bytes from 100.64.0.1: icmp_seq=1 ttl=64 time=38.181 ms

--- 100.64.0.1 ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 37.025/37.603/38.181/0.578 ms
```

也可以使用 Tailscale CLI 来测试：

```bash
$ /Applications/Tailscale.app/Contents/MacOS/Tailscale ping 100.64.0.1
pong from coredns (100.64.0.1) via xxxx:41641 in 36ms
```

对于版本号低于 1.32.0 的 Tailscale 客户端，你只需要按照图中所述的步骤操作即可，本文就不再赘述了。

### Android

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#android)

Android 客户端从 1.30.0 版本开始支持自定义控制服务器（即 coordination server），你可以通过 [Google Play](https://icloudnative.io/go/?target=aHR0cHM6Ly9wbGF5Lmdvb2dsZS5jb20vc3RvcmUvYXBwcy9kZXRhaWxzP2lkPWNvbS50YWlsc2NhbGUuaXBu) 或者 [F-Droid](https://icloudnative.io/go/?target=aHR0cHM6Ly9mLWRyb2lkLm9yZy9wYWNrYWdlcy9jb20udGFpbHNjYWxlLmlwbi8%3d) 下载最新版本的客户端。

安装完成后打开 Tailscale App，会出现如下的界面：

![](https://images.icloudnative.io/uPic/2022-11-22-18-12-m2IYpv.jpeg)

点开右上角的“三个点”，你会看到只有一个 `About` 选项：

![](https://images.icloudnative.io/uPic/2022-11-22-18-14-ghdl4A.jpeg)

接下来就需要一些骚操作了，你需要反复不停地**点开再关闭**右上角的“三个点”，重复三四次之后，便会出现一个 `Change server` 选项：

![](https://images.icloudnative.io/uPic/2022-11-22-18-23-mcAexh.jpeg)

点击 `Change server`，将 headscale 控制服务器的地址填进去：

![](https://images.icloudnative.io/uPic/2022-11-22-18-37-fkRIxW.jpeg)

然后点击 `Save and restart` 重启，点击 `Sign in with other`，就会跳出这个页面：

![](https://images.icloudnative.io/uPic/2024-01-07-19-39-fKOCTT.jpg)

将其中的命令粘贴到 Headscale 所在主机的终端，将 **USER** 替换为之前创建的 user，然后执行命令即可。注册成功后可将该页面关闭，回到 App 主页，效果如图：

![](https://images.icloudnative.io/uPic/2024-01-07-20-21-2e8CKX.jpg)

### Windows

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#windows)

Windows Tailscale 客户端想要使用 Headscale 作为控制服务器，只需在浏览器中打开 URL：`https://<HEADSCALE_PUB_ENDPOINT>/windows`，便会出现如下的界面：

![图片描述: 2023-12-29-17-19-vSqFK9.png](https://images.icloudnative.io/uPic/2023-12-29-17-19-vSqFK9.png)

按照其中的步骤操作即可。

### 其他 Linux 发行版

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E5%85%B6%E4%BB%96-linux-%E5%8F%91%E8%A1%8C%E7%89%88)

除了常规的 Linux 发行版之外，还有一些特殊场景的 Linux 发行版，比如 OpenWrt、威联通（QNAP）、群晖等，这些发行版的安装方法已经有人写好了，这里就不详细描述了，我只给出相关的 GitHub 仓库，大家如果自己有需求，直接去看相关仓库的文档即可。

- OpenWrt： [https://github.com/adyanth/openwrt-tailscale-enabler](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL2FkeWFudGgvb3BlbndydC10YWlsc2NhbGUtZW5hYmxlcg%3d%3d)
- 群晖： [https://github.com/tailscale/tailscale-synology](https://icloudnative.io/go/?target=aHR0cHM6Ly9naXRodWIuY29tL3RhaWxzY2FsZS90YWlsc2NhbGUtc3lub2xvZ3k%3d)
- 威联通： [https://github.com/tailscale/tailscale-qpkg](https://icloudnative.io/go/?target=aGh0dHBzOi8vZ2l0aHViLmNvbS90YWlsc2NhbGUvdGFpbHNjYWxlLXFwa2c%3d)

### iOS

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#ios)

iOS 系统直接从应用商店安装即可，当然前提是你需要有一个美区 ID。

1. 安装完成后打开 Tailscale 确认你没有登录任何账号。然后打开「设置」，向下滑动，在「Game Center」或者「电视提供商」下方找到「Tailscale」，然后点击进去。
    
    ![图片描述: 2023-12-29-17-41-byKA02.png](https://images.icloudnative.io/uPic/2023-12-29-17-41-byKA02.png)
    
    如果你的设备之前登录过 Tailscale 服务端，需要将「Reset Keychain」选项打开。
    
2. 在「Alternate Coordination Server URL」下方输入你的 Headscale 公网域名。
    
3. 从 iOS 应用程序切换器中关闭 Tailscale 再重新打开，然后选择「Log in」，就会弹出一个 Headscale 身份认证页面。
    
    ![图片描述: 2023-12-29-17-51-mErNCd.png](https://images.icloudnative.io/uPic/2023-12-29-17-51-mErNCd.png)
    
4. 将 Headscale 身份认证页面中的命令复制粘贴到 headscale 所在容器的终端中，并将 USERNAME 替换为前面所创建的 user。
    
    ```bash
    $ headscale nodes register --user default --key mkey:1fbd9696ebb03b9394033949514345bc5dba0e570bc0d778f15f92a02d2dcb66
    2023-12-29T09:55:38Z TRC DNS configuration loaded dns_config={"Nameservers":["1.1.1.1"],"Proxied":true,"Resolvers":[{"Addr":"1.1.1.1"}]}
    Node localhost registered
    ```
    
5. 注册成功。
    
    ![图片描述: 2023-12-29-18-01-Z2XdzF.png](https://images.icloudnative.io/uPic/2023-12-29-18-01-Z2XdzF.png)
    

### 通过 Pre-Authkeys 接入

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E9%80%9A%E8%BF%87-pre-authkeys-%E6%8E%A5%E5%85%A5)

前面的接入方法都需要服务端同意，步骤比较烦琐，其实还有更简单的方法，可以直接接入，不需要服务端同意。

首先在服务端生成 pre-authkey 的 token，有效期可以设置为 24 小时：

```bash
$ headscale preauthkeys create -e 24h --user default
```

查看已经生成的 key：

```bash
$ headscale --user default preauthkeys list
ID | Key                                              | Reusable | Ephemeral | Used  | Expiration          | Created            
1  | 57e419c40e30b0dxxxxxxxf15562c18a8c6xxxx28ae76f57 | false    | false     | false | 2022-05-30 07:14:17 | 2022-05-29 07:14:17
```

当然你也可以在 Headscale-Admin 中生成。点击客户端想加入的 User：

![图片描述: 2024-01-07-21-52-baNzjl.jpg](https://images.icloudnative.io/uPic/2024-01-07-21-52-baNzjl.jpg)

在弹出的界面中点击「PreAuth Keys」右侧的 `Create`，设置一个过期时间（比如 100 年~），如果想重复利用这个 Key，可以勾选 `Reusable`，最后点击 ✅：

![图片描述: 2024-01-07-21-57-nSM3jC.png](https://images.icloudnative.io/uPic/2024-01-07-21-57-nSM3jC.png)

创建成功后，点击红框区域便可复制该 PreAuth Key：

![图片描述: 2024-01-07-22-00-ZOw8lm.png](https://images.icloudnative.io/uPic/2024-01-07-22-00-ZOw8lm.png)

现在新节点就可以无需服务端同意直接接入了：

```bash
$ tailscale up --login-server=http://<HEADSCALE_PUB_ENDPOINT>:8080 --accept-routes=true --accept-dns=false --authkey $KEY
```

## 打通局域网

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E6%89%93%E9%80%9A%E5%B1%80%E5%9F%9F%E7%BD%91)

到目前为止我们只是打造了一个点对点的 Mesh 网络，各个节点之间都可以通过 WireGuard 的私有网络 IP 进行直连。但我们可以更大胆一点，还记得我在文章开头提到的访问家庭内网的资源吗？我们可以通过适当的配置让每个节点都能访问其他节点的局域网 IP。这个使用场景就比较多了，你可以直接访问家庭内网的 NAS，或者内网的任何一个服务，**更高级的玩家可以使用这个方法来访问云上 Kubernetes 集群的 Pod IP 和 Service IP。**

假设你的家庭内网有一台 Linux 主机（比如 OpenWrt）安装了 Tailscale 客户端，我们希望其他 Tailscale 客户端可以直接通过家中的局域网 IP（例如 **192.168.100.0/24**） 访问家庭内网的任何一台设备。

配置方法很简单，首先需要设置 IPv4 与 IPv6 路由转发：

```bash
$ echo 'net.ipv4.ip_forward = 1' | tee /etc/sysctl.d/ipforwarding.conf
$ echo 'net.ipv6.conf.all.forwarding = 1' | tee -a /etc/sysctl.d/ipforwarding.conf
$ sysctl -p /etc/sysctl.d/ipforwarding.conf
```

客户端修改注册节点的命令，在原来命令的基础上加上参数 `--advertise-routes=192.168.100.0/24`，告诉 Headscale 服务器“我这个节点可以转发这些地址的路由”。

```bash
$ tailscale up --login-server=http://<HEADSCALE_PUB_ENDPOINT>:8080 --accept-routes=true --accept-dns=false --advertise-routes=192.168.100.0/24 --reset
```

在 Headscale 端查看路由，可以看到相关路由是关闭的。

```bash
$ headscale nodes list|grep openwrt

6 | openwrt | [7LdVc] | default | 100.64.0.6 | false | 2022-03-20 15:50:46 | onlin

e | no

$ headscale routes list -i 6

Route | Enabled

192.168.100.0/24 | false
```

开启路由：

```bash
$ headscale routes enable -i 6 -r "192.168.100.0/24"

Route | Enabled

192.168.100.0/24 | true
```

如果有多条路由需要用 `,` 隔开：

```bash
$ headscale routes enable -i 6 -r "192.168.100.0/24,xxxx"
```

也可以通过参数 -a 开启所有路由：

```bash
$ headscale routes enable -i 6 -a
```

其他节点查看路由结果：

```bash
$ ip route show table 52|grep "192.168.100.0/24"
192.168.100.0/24 dev tailscale0
```

其他节点启动时需要增加 `--accept-routes=true` 选项来声明 “我接受外部其他节点发布的路由”。

现在你在任何一个 Tailscale 客户端所在的节点都可以 ping 通家庭内网的机器了，你在公司或者星巴克也可以像在家里一样用同样的 IP 随意访问家中的任何一个设备，就问你香不香？

## 总结

[#](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#%E6%80%BB%E7%BB%93)

目前从稳定性来看，Tailscale 比 Netmaker 略胜一筹，基本上不会像 Netmaker 一样时不时出现 ping 不通的情况，这取决于 Tailscale 在用户态对 NAT 穿透所做的种种优化，他们还专门写了一篇文章介绍 [NAT 穿透的原理](https://icloudnative.io/go/?target=aHR0cHM6Ly90YWlsc2NhbGUuY29tL2Jsb2cvaG93LW5hdC10cmF2ZXJzYWwtd29ya3Mv)， [中文版](https://icloudnative.io/go/?target=aHR0cHM6Ly9hcnRodXJjaGlhby5hcnQvYmxvZy9ob3ctbmF0LXRyYXZlcnNhbC13b3Jrcy16aC8%3d)翻译自国内的 eBPF 大佬赵亚楠，墙裂推荐大家阅读。放一张图给大家感受一下：

![图片描述: 2022-03-21-10-52-TzXGEZ.png](https://images.icloudnative.io/uPic/2022-03-21-10-52-TzXGEZ.png)

本文给大家介绍了 Tailscale 和 Headscale，包括 Headscale 的安装部署和各个平台客户端的接入，以及如何打通各个节点所在的局域网。下篇文章将会给大家介绍 [如何让 Tailscale 使用自定义的 DERP Servers](https://icloudnative.io/go/?target=L3Bvc3RzL2N1c3RvbS1kZXJwLXNlcnZlcnMv)（也就是中继服务器），See you~~

Tailscale 系列教程 - 本文属于系列文章之一

[](https://icloudnative.io/posts/tailscale-acls/)

[](https://icloudnative.io/posts/custom-derp-servers/)

-------他日江湖相逢 再当杯酒言欢-------

[](https://www.linkedin.com/shareArticle?mini=true&url=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&title=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "分享到 LinkedIn")[](https://twitter.com/intent/tweet/?url=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&text=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "分享到 Twitter")[](https://reddit.com/submit/?url=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&resubmit=true&title=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "提交到 Reddit")[](https://api.whatsapp.com/send?text=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&resubmit=true&title=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "分享到 WhatsApp")[](https://t.me/share/url?url=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&resubmit=true&title=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "分享到 Telegram")[](https://pinterest.com/pin/create/bookmarklet/?url=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&description=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "钉到 Pinterest")[](https://www.facebook.com/sharer/sharer.php?u=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&quote=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "分享到 Facebook")[](mailto:?body=https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/&subject=Tailscale%20%e5%9f%ba%e7%a1%80%e6%95%99%e7%a8%8b%ef%bc%9aHeadscale%20%e7%9a%84%e9%83%a8%e7%bd%b2%e6%96%b9%e6%b3%95%e5%92%8c%e4%bd%bf%e7%94%a8%e6%95%99%e7%a8%8b "通过电子邮件发送")

## 相关文章

[

WireGuard 教程：使用 Netmaker 配置 WireGuard 全互联 (full mesh) 模式

2021年11月9日·3663 字·8 分钟·

网络VPNWireGuardLinuxNetmakerKubernetes



](https://icloudnative.io/posts/configure-a-mesh-network-with-netmaker-2/)[

WireGuard 教程：使用 Netmaker 来管理 WireGuard 的配置

2021年10月18日·3490 字·7 分钟·

网络VPNWireGuardLinuxNetmakerKubernetes



](https://icloudnative.io/posts/configure-a-mesh-network-with-netmaker/)[

WireGuard 教程：WireGuard 的搭建使用与配置详解

2020年7月6日·6947 字·14 分钟·

网络VPNWireGuard



](https://icloudnative.io/posts/wireguard-docs-practice/)[

WireGuard 教程：WireGuard 的工作原理

2020年7月1日·3641 字·8 分钟·

网络VPNWireGuard



](https://icloudnative.io/posts/wireguard-docs-theory/)[

WireGuard 教程：使用 DNS-SD 进行 NAT-to-NAT 穿透

2021年1月28日·6312 字·13 分钟·

网络WireGuard



](https://icloudnative.io/posts/wireguard-endpoint-discovery-nat-traversal/)[

我为什么不鼓吹 WireGuard

2020年12月24日·4201 字·9 分钟·

网络WireGuard



](https://icloudnative.io/posts/why-not-wireguard/)

---

[←在 M1 Macbook 中使用原生 Java 运行 Minecraft2022年2月20日](https://icloudnative.io/posts/minecraft-m1/)[Tailscale 基础教程：部署私有 DERP 中继服务器2022年3月27日→](https://icloudnative.io/posts/custom-derp-servers/)

---

![公众号二维码](https://icloudnative.io/img/wechat-qr.webp)

[↑](https://icloudnative.io/posts/how-to-set-up-or-migrate-headscale/#the-top "返回顶部")

- [标签](https://icloudnative.io/tags/ "标签")
- [分类](https://icloudnative.io/categories/ "分类")

总访客802397

总浏览量1555237

© 2024 米开朗基杨  
本站内容依据 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh) 许可证进行授权，转载请附上出处链接。

构建工具[Hugo v0.120.4](https://gohugo.io/) 托管于[Sealos](https://sealos.run/) CDN[Vercel](https://vercel.com/) 图床[jsDelivr](https://www.jsdelivr.com/) 主题[Blowfish](https://github.com/nunocoracao/blowfish)

本站已经开心运行 1932 天 12 小时 39 分 10 秒

[AI 客服](https://github.com/labring/FastGPT)
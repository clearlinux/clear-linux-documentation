.. _qingcloud:

|CL-ATTR| on QingCloud\* (如何在青云 QingCloud 上创建 |CL| 虚拟主机)
#########################################################################

本教程介绍如何通过青云 QingCloud\* 控制台创建和启动 |CL| 实例以及完成以下任务：

#. 在 QingCloud 系统镜像中找到并选择 |CL| 操作系统。
#. 创建新的公钥和私钥对，以便可以安全地连接到 |CL| 虚拟主机。
#. 启动新的 |CL| 虚拟主机并连接到该主机。
#. 删除 |CL| 虚拟主机。

.. contents::
   :local:
   :depth: 1

必备条件
************

本教程假定您已经完成了如下默认配置：

* 您的环境可以运行 SSH 以访问远程 |CL| 虚拟主机。
* 您知悉浏览器下载文件的绝对路径。
* 您已设置了 QingCloud 的用户帐户，并确保该账户为启用状态，并且已登录到 QingCloud 控制台。 要了解有关青云和设置账户的更多信息，请访问青云官网，网址为 https://www.qingcloud.com/。

在 QingCloud 控制台中选择并启动 |CL| 虚拟主机
**********************************************

#. 在浏览器中在 QingCloud 控制台主菜单中，依次选择 **“计算”** 、 **“主机”**，之后点击图1中所示的 **“创建”** 选项。

   .. figure:: /_figures/qingcloud/QingCloud-1.png
      :scale: 50 %
      :alt: QingCloud 控制台

      图1: QingCloud 控制台
    
   选择此选项后，页面将跳转到“创建主机”页面。

#. 在创建主机页面，先点击图2中所示的 **“系统”** 选项，再点击最右侧 **|CL|** 图标，并点击 **“下一步”** 按钮。 

   .. figure:: /_figures/qingcloud/QingCloud-2.png
      :scale: 50 %
      :alt: 选择 |CL| 创建虚拟主机

      图2: 选择 |CL| 创建虚拟主机

   之后，您将来到配置选择界面。 

#. 在配置选择界面，您可以看到不同硬件配置类型的虚拟主机，比如调整 CPU 核心数量、内存大小以及硬盘和副本备份策略。这里我们将选择默认配置来进行接下来的演示。

   .. figure:: /_figures/qingcloud/QingCloud-3.png
      :scale: 50 %
      :alt: 配置选择

      图3: 配置选择

   在点击 “下一步” 按钮之后，您将来到网络设置界面。

#. 在网络设置界面，您可以创建私有的 VPC 网络，也可以快速测试 |CL| 选择基础网络。 这里我们选择 **“基础网络”**。

   .. figure:: /_figures/qingcloud/QingCloud-4.png
      :scale: 50 %
      :alt: 网络设置

      图4: 网络设置

#. 在基本信息设置界面，您需要输入虚拟主机名称，并设置 SSH 密钥登录方式。

   #. 如果之前没有创建过 SSH 密钥，请点击图5中 **“创建一个”** 按钮以创建 SSH 密钥。

      .. figure:: /_figures/qingcloud/QingCloud-6.png
         :scale: 50 %
         :alt: 创建SSH密钥

         图5: 创建SSH密钥

      在点击 “创建一个” 按钮之后，页面将跳转到 SSH 密钥创建界面。

   #. 在 SSH 密钥创建界面中，您可以依照图6填写密钥的名称以便记忆，并且选择您需要的加密方法，确认无误后即可点击 **“提交”** 按钮。

      .. figure:: /_figures/qingcloud/QingCloud-6.png
         :scale: 50 %
         :alt: 新建SSH密钥

         图6: 新建SSH密钥

      提交之后，将跳出密钥下载按钮。

   #. 出现密钥下载按钮后，请在10分钟之内点击下载按钮完成密钥的下载，并将该密钥妥善保存到本地，以便之后连接虚拟主机使用。

      .. figure:: /_figures/qingcloud/QingCloud-7.png
         :scale: 50 %
         :alt: 下载SSH密钥

         图7: 下载SSH密钥   

      在关闭下载对话框之后，界面将跳转到之前的 “基本信息设置” 界面

#. 在确保 SSH 密钥已妥善下载保存的情况下，如图8检查虚拟主机的基本信息，确认无误后请点击 **“创建”** 按钮。

   .. figure:: /_figures/qingcloud/QingCloud-8.png
      :scale: 50 %
      :alt: 确认信息并创建虚拟主机

      图8: 确认信息并创建虚拟主机

   确认后，QingCloud 将会创建 |CL| 虚拟主机，您可以在新的界面中查看当前虚拟主机的状态。



申请公网IP并添加到虚拟主机
************************************
   
#. 由于 QingCloud 不会为使用默认网络创建的虚拟主机自动分配公网IP地址，所以我们需要手动申请，并添加到虚拟主机。如图9点击导航栏左侧的 **“网络与CDN”** 按钮。

   .. figure:: /_figures/qingcloud/QingCloud-9.png
      :scale: 50 %
      :alt: 网络与CDN

      图9: 网络与CDN

   点击后，您将来到网络与CDN配置界面。

#. 在新页面中，如图10点击左侧 **“公网IP”** 按钮，并点击中间的 **“申请”** 按钮以进行创建公网IP。

   .. figure:: /_figures/qingcloud/QingCloud-10.png
      :scale: 50 %
      :alt: 申请创建公网IP

      图10: 申请创建公网IP

   点击申请后，将跳出提示栏，仔细阅读后按照图11点击 **“继续申请公网IP”** 按钮。

   .. figure:: /_figures/qingcloud/QingCloud-11.png
      :scale: 50 %
      :alt: 提示栏确认

      图11: 提示栏确认

   之后将跳转到申请公网IP界面。

#. 在申请公网IP页面中，如图12确认和填写相关信息，包括计费模式和带宽上限（本教程中使用的是流量计费模式并且设置了2Mbps的带宽上限），确认无误后点击 **“提交”** 按钮。

   .. figure:: /_figures/qingcloud/QingCloud-13.png
      :scale: 50 %
      :alt: 确认提交公网IP申请

      图12: 确认提交公网IP申请

#. 之后如图13通过导航栏点击 **“计算”**、**“网卡”** 按钮来到网卡界面。

   .. figure:: /_figures/qingcloud/QingCloud-13.png
      :scale: 50 %
      :alt: 网卡界面

      图13: 网卡界面

#. 在网卡界面，按照图14选中刚刚创建的 Clear Linux OS 主机的网卡，并点击上方 **“更多操作”** 按钮，再点击 **“绑定公网IPv4”** 按钮。

   .. figure:: /_figures/qingcloud/QingCloud-14.png
      :scale: 50 %
      :alt: 绑定选中

      图14: 绑定选中

#. 在绑定公网IP确认界面，按照图15选择刚刚申请完成的公网IP地址，并点击下方 **“提交”** 按钮。 等待片刻后，状态将会变成图16中所示。

   .. figure:: /_figures/qingcloud/QingCloud-15.png
      :scale: 50 %
      :alt: 提交绑定

      图15: 提交绑定

   .. figure:: /_figures/qingcloud/QingCloud-16.png
      :scale: 50 %
      :alt: 公网IP绑定成功

      图16: 公网IP绑定成功


连接到 |CL| 虚拟主机
*****************************

请您点击导航栏左侧 **“计算”**、**“主机”** 按钮，确认当前虚拟主机处于正在运行状态，且已绑定了公网IP地址。如图17所示。

.. figure:: /_figures/qingcloud/QingCloud-17.png
   :scale: 50 %
   :alt: 确认虚拟主机当前处于正常状态

   图17: 确认虚拟主机当前处于正常状态

#. 复制当前 |CL| 虚拟主机的公网IP地址，并使用 SSH 客户端进行连接。 这里我们需要用到之前保存的 SSH 密钥。
#. 在此教程中，以 MobaXterm 客户端为例演示登录过程。请如图18检查各项。用户名我们选择 **root**，密钥请选择之前下载并保存到本地的 SSH 密钥。

   .. figure:: /_figures/qingcloud/QingCloud-18.png
      :scale: 50 %
      :alt: SSH 登录虚拟主机设置

      图18: SSH 登录虚拟主机设置

#. 设置成功后，点击登录即可登录到 |CL| 虚拟主机。
   
   .. figure:: /_figures/qingcloud/QingCloud-19.png
      :scale: 50 %
      :alt: SSH 登录成功

      图19: SSH 登录成功


删除 |CL| 虚拟主机
*************************

本章节介绍如何在 QingCloud 上删除所创建的 |CL| 虚拟主机。

#. 通过左侧导航栏依次选择 **“计算”**、**“主机”** 后，找到刚刚创建的 Clear Linux OS 主机，如图20所示选中此主机，再点击上方 **“更多操作”** 按钮选择 **“删除”**，即可删除虚拟主机。

   .. figure:: /_figures/qingcloud/QingCloud-20.png
      :scale: 50 %
      :alt: |CL| 虚拟主机

      图20: 删除 |CL| 虚拟主机


删除申请的公网IP
*****************

本章节介绍如何在 QingCloud 上删除所申请的公网IP地址。

#. 通过左侧导航栏依次选择 **“网络与CDN”**、**“公网IP”** 后，找到刚刚申请的公网IP地址，如图21所示选中此项目，再点击上方 **“更多操作”** 按钮选择 **“删除”**，即可删除。

   .. figure:: /_figures/qingcloud/QingCloud-21.png
      :scale: 50 %
      :alt: 删除公网IP地址

      图21: 删除公网IP地址
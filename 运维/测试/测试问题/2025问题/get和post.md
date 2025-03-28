# GET请求

示例
场景：查询用户信息

* URL正确性
* 参数传递：验证查询字符串中的参数是否能够正确的被服务器识别和解析
* 缓存机制：GET请求通常会被浏览器或代理服务器缓存。测试时应该考虑不同的缓存策略是否影响了数据的新鲜度
* 安全性：敏感信息不应该通过GET请求传输，因为他们会显示在URL，容易被记录和拦截
* 响应内容：确定返回的数据格式（JSON，XML）符合预期，并且数据是正确的

## POST请求
场景：提交新用户注册信息

* 数据完整性：验证发送到服务器的数据完整性和准确性，比如，在注册表单中提交的所有字段是否都被正确接受
* 请求体格式：确保请求体（JSON， XML）以及编码方式 UTF-8 与服务器期望的一致
* 状态码检查：POST操作成功后，应该收到200OK，201Created等表示成功的状态码，失败时应该有目前的状态码说明问题
* 重复提交问题：防止由于网络延迟等原因导致的重复提交，可以测试按下按钮多次提交后的系统行为
* 安全性：POST请求用于提交敏感信息时，想要使用HTTPS保证数据加密传输，同时注意防止CSRF攻击（跨站请求仿造）
* 

## 共同点
错误处理：无论是GET还是POST请求，都需要测试当遇到无效输入或者异常情况时，系统的错误处理能力，包括但不限于返回适当的HTTP状态码、友好的错误消息等。
性能测试：对于频繁使用的API接口，还需要关注其性能表现，比如响应时间、吞吐量等指标。
兼容性测试：确保不同版本的客户端与服务器之间的通信没有问题，尤其是涉及向前向后兼容的情况。



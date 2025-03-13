# 上传文件大小限制
上传失败的话，需要清理缓存
有时候，Git会在.git/objects/pack/中留下一些临时的或损坏的包文件。
```
git gc --prune=now
```

github单文件最大不能超过 100MB
# get_info_from_dwg
- 借助dwg2dxf.exe，获取cad中dwg格式文件的信息
- 目前没有直接解析dwg文件的python库，所以在此提供一个思路：先将dwg转为dxf文件，在读取dxf文件里的信息
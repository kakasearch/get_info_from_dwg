import ezdxf
import os
import subprocess
import re

def read_dxf(dxf_path):
    #返回dxf文件中一条多段线的坐标,dxf
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()
    for entity in msp:
        if entity.dxftype() == 'LWPOLYLINE':
            points = entity.get_points('xy')
            return points
        elif entity.dxftype() == 'LWPOLYLINE':
            points = entity.get_points('xy')
            return points
        else:                                                              
            pass
    return []
def dwg2dxf(dwg_path,dxf_path):
    #调用同目录下的dwg2dxf，将dwg转为dxf文件。需要指定-v2004，没有这个参数会造成dxf信息缺失
    cmd = f'dwg2dxf {dwg_path} -v2004 -y {dxf_path}'
    try:
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE).stdout.decode('utf-8')
    except:
        print("dwg转换错误")  # 打印返回结果

def main(dwg_path):
    #获取其中一个多段线的坐标
    if "dwg" not in dwg_path:
        print("非dwg文件")
        return
    dxf_path = dwg_path.replace(".dwg",".dxf").replace(" ",'')
    dwg2dxf(dwg_path,dxf_path)
    txt_path = dwg_path.replace(".dwg",".txt")
    filename = os.path.splitext(os.path.basename(dwg_path))[0]

    coords = read_dxf(dxf_path) #只会读第一个多段线
    if not coords:
        print("dwg读取错误")
        return 
    with open(txt_path,"w",encoding="utf-8")as f:
        f.write(str(coords))
    #删除dxf文件
    os.remove(dxf_path)
    print("处理完毕",filename)


if __name__ == '__main__':
    print("\t\t dwg数据获取示例")
    files = input("\n请拖入要处理的dwg文件:").strip()
    main(files)
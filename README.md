# 用法
根据设定的前缀与后缀从文档中提取数据    
python getdata.py -t 数据文件 [-o 输出文件] -p "前缀" -s "后缀"    

# 注意
注意前后缀中如果需要匹配双引号 **\"** 需要增加转义符 **\\\"**    

# 示例
    {
    "phone:18888888888"
    "phone:13888888888"
    "phone:13111111111"
    }

提取文档中所有phone的数值    
python getdata.py -t 数据文件 [-o 输出文件] -p \"\\\"phone:\" -s \"\\\",\"    

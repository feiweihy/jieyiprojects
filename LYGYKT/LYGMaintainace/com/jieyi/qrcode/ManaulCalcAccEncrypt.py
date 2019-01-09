import socket,binascii

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8018
client.connect((host, port))

# 字符串形式的命令转化为要发送的byte数组
def asc2byte_strmsg(send_msg):
    send_msg_len = len(send_msg)
    send_msg_byte = binascii.b2a_hex(send_msg.encode())
    send_msg_bytehex = send_msg_byte.decode()
    send_msg_bytehex = str(send_msg_len).zfill(4) + send_msg_bytehex
    return binascii.a2b_hex(send_msg_bytehex)

# send_msg = 'EJS02'
# send_msg_len = len(send_msg)
#
# send_msg_byte = binascii.b2a_hex(send_msg.encode())
# send_msg_bytehex = send_msg_byte.decode()
#
# send_msg_bytehex = str(send_msg_len).zfill(4)+send_msg_bytehex
#
# print(send_msg_bytehex)
# print(binascii.a2b_hex(send_msg_bytehex))

# 加密机应该以hexstr进去，再以hexstr出来
client.send(asc2byte_strmsg('EJS02'))
recvmsg = client.recv(1024)
print (recvmsg)

recvmsg_bytehex = binascii.b2a_hex(recvmsg)
# recvmsg_bytehexstr = recvmsg_bytehex.decode()
# print(recvmsg_bytehexstr)
# print(recvmsg_bytehex[8:12])
# print(recvmsg_bytehex[8:12].decode())
result = (binascii.a2b_hex(recvmsg_bytehex[8:12].decode())).decode()

publickey_uncompressed = recvmsg_bytehex[12:].decode()
print(publickey_uncompressed)
x = publickey_uncompressed[0:64]
y = publickey_uncompressed[64:]

# print(binascii.a2b_hex(y[62:])[0]&1)
print(result)

# fuc_calc_publickey_uncompressed = lambda x, y: '03'+x if binascii.a2b_hex(y[62:])[0]&1==1 else '02' + x
# print(fuc_calc_publickey_uncompressed(x,y))

publickey_uncompressed = '03'+x if binascii.a2b_hex(y[62:])[0]&1==1 else '02' + x
# publickey_uncompressed = '03'+x if binascii.a2b_hex('F6')[0]&1==1 else '02' + x
print(publickey_uncompressed)


client.close()
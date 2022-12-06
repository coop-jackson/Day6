
#the start of a packet is indicated by a sequence of four characters that are all different.


#bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
#nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
#nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
#zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

#part 1 and 2
        
def unique_elements(num, line):
    buffer = [''] * num
    differ = False
    for i, c in enumerate(line):
        buffer.pop(0)
        buffer.append(c)
        for z in buffer:
            if buffer.count(z) > 1 :
                differ = False
                break
            if buffer[0] != '':
                differ = True
        
        if differ:
            return i + 1
            
with open('packet_stream.txt') as file:
    line = file.readline()
    print(unique_elements(4,line))
    print(unique_elements(14,line))





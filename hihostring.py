def main():
    while True :
        
        inputs = raw_input().split()
        if len(inputs) == 0:
            break
        else:
            a, b = [int(d) for d in inputs]
            print a + b
            
if __name__ == '__main__':
	main()
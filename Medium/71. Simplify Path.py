class Solution:
    def simplifyPath(self, path: str) -> str:
        res: str = ''
        dir: str = ''
        stack: list[str] = []
        for i in range(len(path)):
            if path[i] != '/':
                dir += path[i]
            elif dir != '':
                if dir == '..' and len(stack) > 0:
                    stack.pop()
                elif dir == '.':
                    dir = ''
                elif dir != '..':
                    stack.append(dir)
                dir = ''
            path[i]

        if dir != '':
            if dir == '..' and len(stack) > 0:
                stack.pop()
            elif dir == '.':
                dir = ''
            elif dir != '..':
                stack.append(dir)
            dir = ''

        for i in range(len(stack)):
            res = '/' + stack.pop() + res

        return res if res != '' else '/'
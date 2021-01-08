R,C=map(int,input().split())
S=[input() for c in range(R)]
visited_area=[[-1]*C for _ in range(R)]
visited_area[sy-1][sx-1]=0
stack=[[sy-1,sx-1]]
def bfs(S,visited_area,stack):
    while len(stack)>0:
        h,w=stack.pop()
        if h==gy-1 and w==gx-1:
            return visited_area[h][w]
        for x,y,in ([1,0],[-1,0],[0,1],[0,-1]):
            new_h=h+x
            new_w=w+y
            if new_w<0 or new_w>=C or new_h<0 or new_h>=C:
                continue
            if S[new_h][new_w]=='.' and visited_area[new_h][new_w]==-1:
                visited_area[new_h][new_w]=visited_area[h][w]+1
                stack.insert(0,[new_h,new_w])


# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:00:49 2017

@author: Madhura Kashikar
"""

import pygit2
#import subprocess


repo = pygit2.Repository('C:/Users/Madhura Kashikar/Desktop/Trial/tacotron/')
print(repo.path)
print(repo.workdir)

print("\n")

commit = repo[repo.head.target]
name_a=[]
commit_list=[]
last = repo[repo.head.target]




for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    
    name_a.append(commit.author.name)
    #print(name_a)
    name_a = list(set(name_a))
    commit_list.append(commit.tree_id.hex)

num=len(name_a)


num1=len(commit_list)

for x, y in zip(commit_list, commit_list[1:]):
    diff=repo.diff(x,y)
    patches=[p for p in diff]
    print("\n \t",patches)
    print("\n \t",diff.patch)
    DiffStats.insertions(diff)
    
    #k=diff._iter_()
    #diff._len_
    
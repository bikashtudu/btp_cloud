user_login(root,vm2).

users(root).
users(prasad).
users(gdm).

vm(vm1).
vm(vm2).
vm(vm3).

access(root,[vm1,vm2]).
access(prasad,[vm2,vm1]).
access(gdm,[vm2]).

access_check(X,[X|_]).
access_check(X,[_|Tail]):- access_check(X,Tail).

access_granted(X,Y):- access(X,Z),access_check(Y,Z).

check(X,Y):-users(X),vm(Y),access_granted(X,Y).

sla():- forall(user_login(X,Y),check(X,Y)).

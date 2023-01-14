#Make a list of unconfirmed users.
unconfirmed_users=["erica","eager","jessy","pius"]
confirmed_users=[]

#verify and append user to the confirmed list when confirmed.
while unconfirmed_users:
	current_user=unconfirmed_users.pop()
	print("verifying user:"+" "+current_user.title())
	confirmed_users.append(current_user.title())
	

#Display confirmed users.
print("The following users have been confirmed:")	
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
	


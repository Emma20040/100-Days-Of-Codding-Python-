enemies = 1

def increase_enemies():
    # modifing the global variable eniemies
    global enemies 
    enemies += 2
    print(f"enemies inside the function {enemies}")

increase_enemies()
print(f"enemies outside the function {enemies}")
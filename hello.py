
def attack(name, location, damage):
    print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

name = "보병"
hp = 40
damage = 5

print("{} 유닛을 생성했습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp,damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛을 생성했습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛을 생성했습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp,tank2_damage))

attack(name, "1시", damage)
attack(tank_name, "11사", tank_damage)
attack(tank_name, "11사", tank2_damage)
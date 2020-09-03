p = "0xc315d99cf91a018dafba850237935b2d981e82b02d994f94db0a1ae40d1fc7ab9799286ac68d620f1102ef515b348807060e6caec5320e3dceb25a0b98356399"
q = "0xe90bbb3d4f51311f0b7669abd04e4cc48687ad0e168e7183a9de3ff9fd2d2a3a50303a5109457bd45f0abe1c5750edfaff1ad87c13eed45e1b4bd2366b49d97f"

int_p = int(p, 16)

int_q = int(q, 16)

product_int = int_p * int_q

product_hex = hex(product_int)

print product_hex

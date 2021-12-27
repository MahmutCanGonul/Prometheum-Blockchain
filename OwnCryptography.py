 
def Encrypted(amount):
    alphabets = string.ascii_letters 
    digits = string.digits
    alpha = []
    result=""
    for i in range(len(alphabets)):
        result = ""+alphabets[i]
        if result.isupper():
            break
        else:
            alpha.append(alphabets[i])
    alpha.append('ı')        
    alpha.append('ö')
    alpha.append('ü')
    alpha.append('ç')
    alpha.append('ğ')
    
    for i in range(len(digits)):
        alpha.append(digits[i])
    
    for i in range(len(punctuation)):
         alpha.append(punctuation[i])
    
     
    #Don't forget add ü,i,ö chars
    codes = {'1ANk1EeLjUbw29vzfzfvZjb7frThog8EpqwehVP0X08QQVWwPY6fWNYFJRiq_ju9954MLGXozaa14jTBKUM6sek_cGaYLKsq7zTIykSEuDwEaI0Y0jhP6Vg⣿':alpha[0],
             'L2ZpJ4rSNPWGgAqRavUv4ZCJTUM5uDbCpLABB3m3SrskVkTehd4GNMP6AvSaMpkepq7QnuPRPCNDZiEiiraf7o1NLvodC5tsVk-kSdaIpNADIJvGCrtvvzZ⣿':alpha[1], 
             '1y8kVM47RuhRGfqaJovngFWKMDw8UvwMiQ8ScPmM3XwGUtnzk9PoNrYCj-Y3RRwDjrwwBi8hF52WitkaJXOfVFHvv-c6XZjmKNurxwMB-5Qx9pIRUXVsXie⣿':alpha[2],
             'KwrFuz3ETNcacYnt99AaoP64HbTkzJzg81TehLHtDqqM3iR6hCVjNMd0aZP80zepGDpYkIkS3O-iDT2MPTm_8_JpEMOFLQBfqSfPWqkD_KUAKJPsM8UrfdM⣿':alpha[3],
             'b9091ec7b189de122b73291625c4d2a6c723bb76a87043e4723e9a679e0fae30Munf-pmmM_wMgQN2ltqE49C5U1jUK0pg3rPqF9cy5Xk83xV6KTiH3jW⣿':alpha[4], 
             'a112f18140b79efd2e95342fc308ad1140b4080d6fef74affc1f281f39427f56QImixVAxGm0d6vdynL71xVMUchuQ0_IOSIVWGYWl0fvyDQKq4lB2K-k⣿':alpha[5], 
             '8d057ac3a67e6714183e778d1cb02d32085cce244088725b7fde552e1459a8edgJfx6DFue2Y19BMe5puBGLpVcVCvZXUYynU-OAPWNNzvghRhtPej9x7⣿':alpha[6], 
             '93bc19abdc36c50be13e1b8e2302d6bad0626c0d5a480678c9592c6febfb751c_J14VyLkPo0IPQaogBarFUaPDrMDJaWQjWlv0Nh2zvZWJgT2TZEU0_9⣿':alpha[7], 
             '778f6f9631ab2543900f5ed1a3d89dd920f0493b5f4b3ffbce98c0bd99dceb20-f9xvnkAY5qY2xNJU0T81xpaIO-5_GAWApph3rus_-hZI-kfPVMZ7cm⣿':alpha[8], 
             'eaec26a596e586e4bed164c1c8dddfaec6d3ca7d6a22115f1d9783923b225d788iGIaMQSch8Hc3cI7RQHtOx0EADIilyUzXcQDtMXchwNgRaZnqED_QE⣿':alpha[9], 
             '7741724df098c0827cb84c5811dfa6297e6edd7db99e7ba73e5b41e3b3e0bc99h4PyPoNMsercOGqkMZScAZV2UnJQLNgRvGg2InLYQk7vfJaKMHf1dhM⣿':alpha[10], 
             '422e773929235813e0a62b09d9f9c0c4f22aecf1839ff47f6fcc98f11183adc0ZNGvJsvRmI2zfD8aoUa3OLgjMjAwESVPxU7e_kMQTHLpevt7mNUvTZp⣿':alpha[11], 
             '0c0082dcbfea0f96b70f25762cc530926284c5aff65c5d0bd405e613a921f56eMyCsOPDtlQOV-sXjplhfWO561BBel0_qBNyhrMyYK-S0QLsct9oQyqB⣿':alpha[12], 
             'd5a30cbb6e3a06bbf02c428e0575802150b6b10437f2d5c2cfa5b60e5ba1d965Vocp8NrL1YH9AkN2rIvNfOysNQ2cCEMlFRmLP4tsvrwAPwJ8J-J-m_O⣿':alpha[13], 
             '1708625668a5c44184770358ad32b41a5ebec93bde3eaeba87b700e017b68305V0hVGo1WCJPyuWpOZ4gX2ddgl8EKdMlzwZVDGZiIN6G_E8mz2-2fA8G⣿':alpha[14], 
             '7078e2646f024b4ee0c291c4f94ee5bd3f4aa1ba3b7e4db3b364631fd7259571pkPwUXo7uGwBIq6IrtoP-PgfD_FF-Vl321WCXDs_imyuZYRpK9AI1Dv⣿':alpha[15], 
             '4fbccd467afcc8508e1b1249f8358e357ba354201a105d208b28fddbd01022daoaj1ckkYzgEEH9X9H-51Rea4ooxy-A2ScGYLDE-Aqfjrns2Rg_KSdM_⣿':alpha[16], 
             '97a115722a2cb052e7b27351f568b452d465de1c4cb994d3d52c6ca4fd386edazCgVXjsCj7sEOSiBXk7KyKxd4RKBgVCCNxY2QIE9whNwK7XaLJjSeU2⣿':alpha[17], 
             '73b9b3faea927b6b1a94ecda5376b6ab507b202d21755e59b0cf56d5ce04ff0a-wjVLL4NZ7rNkR9WlaJidzN1PkELOOTiaEyTmwDwaD4sBk0voU_PU3w⣿':alpha[18], 
             '235f39325a9dbc7648822ce6c3dc214810416fb55020bbc4e09d2d734e13219c68k3cJJZhi8CNeFsOas7749Z7LgWwXY_Cog1KQjmWRJXy87foj1VG24⣿':alpha[19], 
             'g8454bf91ffae1b0876839ca5846384049ca6eb9c3af666d16fef94d4f5b3ca7b_Av9nEB_1YyVoepsr0nIRjvE6-l9hdXmZz4LUjcf2ECS8P4fdT4luw⣿':alpha[20], 
             'AAB23c538104a7963f5d1bb9da037f9935c42f1fa2f8c8ddb1fe7b5ef605400ab79piiHdp7tAjlzvI5I9fkt3szt17rftUXggc3KkYEf5YBO2J48BLep⣿':alpha[21], 
             'B63c23da0f9ab3e600a1393e71fb87d48603ce08cf1c0e34468e6f4216878e2d8FU_9eohS6XH_REfuhS7n5BlrJdDM2kfLnYB9gw_oB2SBdhas1qRQEQ⣿':alpha[22], 
             '95bc603278dea260cd0612ff9865b0908cb330c6ddb4b17832313a738433df17NM4J6gerzkQAWEDV93tawPJ9eY7zII-DuJ8HQM7Ljk3LLnVMU4IXf60⣿':alpha[23], 
             '7dbed888e53e09e4ea0946f0687654f6b986f20842cb49e8cfc43fcecdb168d3NuESGJ_0stMrkHzvRgeeK0GKyG0_OFeCzE3Ed9oyEg-WRoKKNWYu-G4⣿':alpha[24], 
             '239a2c66ea0b7bcf8b3d157a4a950bbce090700731941eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHCW6iGKP3qL6qkqadXD⣿':alpha[25],
             '048ed5a32944e0cf9124bbfdc4d2c39fc03b3aa59dad85ddc3e53c2e3739ab9a58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHCW6⣿':alpha[26],
             'dfc77c639b0820da9d3e80d8db6bea4bb46683b4d4ead6b8d70b6f70d6ae4b96ee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHC⣿':alpha[27],
             '1Ctfrhv2HHFMpBRJSYB3ACvtq15gYv1Ths741eaee51Cw3BiJ6KJyrwj9u9t7rhxtgJd7bSFX4Av8c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0Lsy⣿':alpha[28],
             'af33bf07421df8947ffb8789e103f1433b49925411738d2d7c5e0d5cd611277c6d741eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqR⣿':alpha[29],
             'bea53353a314db32f93335017f60495ac6e222fd69b1ff87a9def1ec1843c6461eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHe⣿':alpha[30],
             '008e134f5caf483479da95f20869f86becff97ffd4f97f4b3cf1568668c2244b835408ae2dbd11c265f1b9bf9dde390b11182dfdf6d741eaee58c4f⣿':alpha[31],
             'f21c200b6030e109201b7031cab4ce827d7c0deac8ea621c564a8d524734a8bd35ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1⣿':alpha[32],
             '641c3b28f5347e185ed63f2990b09a2d13dabd99c69ed8d454294464169e2db95ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1R⣿':alpha[33],
             'bf149bf660fadbd4cafd813f57357906cd19de107afc9bc236065c5a18ff76735ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1P⣿':alpha[34],
             '95094a1d7d22fcf0dc70577cf5a8257047bb7fe09d4ad2de814ae170be93ac20416354504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3G97⣿':alpha[35],
             '2cbbeb977464ca8cd9c9fac1c74df63e37aa0c2a1f8a57eedf70b4df976f16744504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3G97Ft129⣿':alpha[36],
             '45a1e02612d9e35e8ff9a5944e98dd15631ed3ffea487b08f1604abd1e28367713635ad615416354504e201182dfdf6d741eaee58c4fd08604814bV⣿':alpha[37],
             '71bdde7634edd97dda6677364373b617ef26e1434a8185b208494bcd83d3188a615416354504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3⣿':alpha[38],
             '4c392e0f2cefbfc16ed649b176bd8d277cdcc5d8d233c95451bbf362f46198aa15416354504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3G⣿':alpha[39],
             '76873fc39bcfc40723ba8330fe963fc1e3ca1c4441be25c4ef7b1a3cccc292f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1R⣿':alpha[40],
             'e456744a81dc975ed7a0e59df9f5134f9801310671f9793cfaa7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bV⣿':alpha[41],
             '666b246dbc764c19be22279150812ec3941014fd4cc317478d206751564f70f91ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd08⣿':alpha[42],
             'de5ac1306b1719848cf85c93f2b8b6ab3167feadf41066942c116dd4261ef723f5134f9801310671f9793cfaa7011b1ffd80d892f65ad6154163545⣿':alpha[43],
             '0d1e4ab8b251a45b840505d9569c243ecc2705b8911cfd0df29e7655967f35dea7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58⣿':alpha[44],
             '55fd5164acd2e579b0edd90cfbf48f849f1cdaf63a0a0e5ae9a106656ccb8bd55134f9801310671f9793cfaa7011b1ffd80d892f65ad61541635450⣿':alpha[45],
             'ee5683595b2e8dbea62ffe35ac5636302790b95700c86c2e3383cb29d24bcd90faa7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee⣿':alpha[46],
             '43e36bbeab1426f432875067006b63b08c923d6c9f14642a7c699dd5b9168a0f9793cfaa7011b1ffd80d892f65ad615416354504e201182dfdf6d74⣿':alpha[47],
             'f9a79777aea7e77a679932538703fd4e9dcfb173960d3a25c5ce439d67da152e011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4⣿':alpha[48],
             'aed835507db62b44bfbb6c2acd4d79b1dc81e0d36d765d414ee82a7f3f1f0eaf1b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd⣿':alpha[49],
             'da104677df9ba78778195b8b94024ebfe939fb6198611db48a18d3f83ce96e7f7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c⣿':alpha[50],
             '1fbead09f5c5e008febb8af9a6613df35e154d26dfa9a79821b3eb489a7a7b79fd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd0860⣿':alpha[51],
             '073e733b151e486400c803835605c0dc0b34bd717df6d8f81e0f6c19f04bfbf21ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd08⣿':alpha[52],
             '368eed2e91d916297c4efa7d1aa6be2b2fb4d4a4ddae142fef1b1c43b52effb00d892f65ad615416354504e201182dfdf6d741eaee58c4fd0860409⣿':alpha[53],
             '3804fe5f96182ec5f98e563e25aa518c001a8491ff70899ccfa060a170f842d3d615416354504e201182dfdf6d741eaee58c4fd08604814bV010125⣿':alpha[54],
             '9de8da0d7e8a97789a23ed1f52d7b4414f02d5297221724c7f279349b7a3ccb780d892f65ad615416354504e201182dfdf6d741eaee58c4fd086048⣿':alpha[55],
             'a5b43678d1d31dde06d6c435ff5fb3f6b39277a59628b5ca553eabb9b198c876f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bV01⣿':alpha[56],
             '7fd3ecee53a2f701a05f5c489b80a8c57a13a706992cbf14e7b937a500b414121b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd⣿':alpha[57],
             '786b04f6e34a2fd21b3aae2f94889864025d008025a365b6733680a707ef76b5f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bV01⣿':alpha[58],
             '9c3dcd25fe4acf53a3b1b3d9575b458145fd7189ff1e61a052a7ece74bd2799a0d892f65ad615416354504e201182dfdf6d741eaee58c4fd0860481⣿':alpha[59],
             '6cc5129e82a9c39868660dfbcf7905b8d8d47d452b97bf41303ffdedb8d6b642aa7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee5⣿':alpha[60],
             'cef322fc485203c7a6fd23088e4cf8ddc703b24a6b1799ea2a8f7d510d06f0c3011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4⣿':alpha[61],
             '841e8cd86a7a643906fe4f082ddd094c85503dfc3652d01d8a0bb97732d05295b87216b3330a780794d1680d892f65ad615416354504e201182dfdf⣿':alpha[62],
             'e74f24ec2afdae83f2bafda4fea5ca893bfc21ee614a148e3286106c2d210394d1680d892f65ad615416354504e201182dfdf6d741eaee58c4fd086⣿':alpha[63],
             '3fa8ed81b79e8905990e7123813401dc2c199e0e29a999aadee67e44ac0e2ed687216b3330a780794d1680d892f65ad615416354504e201182dfdf6⣿':alpha[64],
             'f1b94fd3af2d764ae4277470e822acba347b56d8bdbfbdf50519c0717c3879106fb87216b3330a780794d1680d892f65ad615416354504e201182df⣿':alpha[65],
             '37bf6c9cea9307bf8933501bc4eac7935161686f269d9bd02c6e14b0b599414930a780794d1680d892f65ad615416354504e201182dfdf6d741eaee⣿':alpha[66],
             '67dfcf9f6169aacd59ce47d9744ec2b6f8b1a29727681f0d818c75abcb51b6a9330a780794d1680d892f65ad615416354504e201182dfdf6d741eae⣿':alpha[67],
             '8e3486aaf3aa840f90ea0ebe9c9908f720f4bde6c51ac4d170c8f29b0228596d330a780794d1680d892f65ad615416354504e201182dfdf6d741eao⣿':alpha[68],
             '67286991c9ffda7f718ef5120c091d45b5fb1e143671821e4c07d84a97c5eacda780794d1680d892f65ad615416354504e201182dfdf6d741eaee51⣿':alpha[69],
             'fa5f665dae68d1a93f3366dc3b94de6e80b945ac5bd0e034dc84df805427d95b6b3330a780794d1680d892f65ad615416354504e201182dfdf6d741⣿':alpha[70],
             '771db49534bbde8fa5b7495fe3d99a2ee7659e503b7fdbc1115a981c6f0603b03330a780794d1680d892f65ad615416354504e201182dfdf6d741e1⣿':alpha[71],
             '18188db49534bbde8fa5b7495fe3d99a2ee7659e503b7fdbc1115a981c6f0603b03330a780794d1680d892f65ad615416354504e201182dfdf6d741⣿':alpha[72],
            
             }
    key_codes = list(codes.keys())
    message = amount
    message = message.lower()
    enc=""
    decs=[]
    isFound=False
    
    for i in range(len(message)):
        isFound=False
        for j in range(len(alpha)):
            if alpha[j] == message[i]:
                decs.append(key_codes[j])
                isFound=True
                break
        if isFound==False:
            decs.append(message[i])
                
            
    for i in range(len(decs)):
        enc+=decs[i]
    
    
    return enc
    
   
def Decrpyted(amount):
    alphabets = string.ascii_letters 
    digits = string.digits
    alpha = []
    result=""
    for i in range(len(alphabets)):
        result = ""+alphabets[i]
        if result.isupper():
            break
        else:
            alpha.append(alphabets[i])
    
    alpha.append('ı')   
    alpha.append('ö')
    alpha.append('ü')
    alpha.append('ç')
    alpha.append('ğ')
          
     
    for i in range(len(digits)):
        alpha.append(digits[i])
    for i in range(len(punctuation)):
        alpha.append(punctuation[i])
    
    #Don't forget add ü,i,ö chars
    codes = {'1ANk1EeLjUbw29vzfzfvZjb7frThog8EpqwehVP0X08QQVWwPY6fWNYFJRiq_ju9954MLGXozaa14jTBKUM6sek_cGaYLKsq7zTIykSEuDwEaI0Y0jhP6Vg⣿':alpha[0],
             'L2ZpJ4rSNPWGgAqRavUv4ZCJTUM5uDbCpLABB3m3SrskVkTehd4GNMP6AvSaMpkepq7QnuPRPCNDZiEiiraf7o1NLvodC5tsVk-kSdaIpNADIJvGCrtvvzZ⣿':alpha[1], 
             '1y8kVM47RuhRGfqaJovngFWKMDw8UvwMiQ8ScPmM3XwGUtnzk9PoNrYCj-Y3RRwDjrwwBi8hF52WitkaJXOfVFHvv-c6XZjmKNurxwMB-5Qx9pIRUXVsXie⣿':alpha[2],
             'KwrFuz3ETNcacYnt99AaoP64HbTkzJzg81TehLHtDqqM3iR6hCVjNMd0aZP80zepGDpYkIkS3O-iDT2MPTm_8_JpEMOFLQBfqSfPWqkD_KUAKJPsM8UrfdM⣿':alpha[3],
             'b9091ec7b189de122b73291625c4d2a6c723bb76a87043e4723e9a679e0fae30Munf-pmmM_wMgQN2ltqE49C5U1jUK0pg3rPqF9cy5Xk83xV6KTiH3jW⣿':alpha[4], 
             'a112f18140b79efd2e95342fc308ad1140b4080d6fef74affc1f281f39427f56QImixVAxGm0d6vdynL71xVMUchuQ0_IOSIVWGYWl0fvyDQKq4lB2K-k⣿':alpha[5], 
             '8d057ac3a67e6714183e778d1cb02d32085cce244088725b7fde552e1459a8edgJfx6DFue2Y19BMe5puBGLpVcVCvZXUYynU-OAPWNNzvghRhtPej9x7⣿':alpha[6], 
             '93bc19abdc36c50be13e1b8e2302d6bad0626c0d5a480678c9592c6febfb751c_J14VyLkPo0IPQaogBarFUaPDrMDJaWQjWlv0Nh2zvZWJgT2TZEU0_9⣿':alpha[7], 
             '778f6f9631ab2543900f5ed1a3d89dd920f0493b5f4b3ffbce98c0bd99dceb20-f9xvnkAY5qY2xNJU0T81xpaIO-5_GAWApph3rus_-hZI-kfPVMZ7cm⣿':alpha[8], 
             'eaec26a596e586e4bed164c1c8dddfaec6d3ca7d6a22115f1d9783923b225d788iGIaMQSch8Hc3cI7RQHtOx0EADIilyUzXcQDtMXchwNgRaZnqED_QE⣿':alpha[9], 
             '7741724df098c0827cb84c5811dfa6297e6edd7db99e7ba73e5b41e3b3e0bc99h4PyPoNMsercOGqkMZScAZV2UnJQLNgRvGg2InLYQk7vfJaKMHf1dhM⣿':alpha[10], 
             '422e773929235813e0a62b09d9f9c0c4f22aecf1839ff47f6fcc98f11183adc0ZNGvJsvRmI2zfD8aoUa3OLgjMjAwESVPxU7e_kMQTHLpevt7mNUvTZp⣿':alpha[11], 
             '0c0082dcbfea0f96b70f25762cc530926284c5aff65c5d0bd405e613a921f56eMyCsOPDtlQOV-sXjplhfWO561BBel0_qBNyhrMyYK-S0QLsct9oQyqB⣿':alpha[12], 
             'd5a30cbb6e3a06bbf02c428e0575802150b6b10437f2d5c2cfa5b60e5ba1d965Vocp8NrL1YH9AkN2rIvNfOysNQ2cCEMlFRmLP4tsvrwAPwJ8J-J-m_O⣿':alpha[13], 
             '1708625668a5c44184770358ad32b41a5ebec93bde3eaeba87b700e017b68305V0hVGo1WCJPyuWpOZ4gX2ddgl8EKdMlzwZVDGZiIN6G_E8mz2-2fA8G⣿':alpha[14], 
             '7078e2646f024b4ee0c291c4f94ee5bd3f4aa1ba3b7e4db3b364631fd7259571pkPwUXo7uGwBIq6IrtoP-PgfD_FF-Vl321WCXDs_imyuZYRpK9AI1Dv⣿':alpha[15], 
             '4fbccd467afcc8508e1b1249f8358e357ba354201a105d208b28fddbd01022daoaj1ckkYzgEEH9X9H-51Rea4ooxy-A2ScGYLDE-Aqfjrns2Rg_KSdM_⣿':alpha[16], 
             '97a115722a2cb052e7b27351f568b452d465de1c4cb994d3d52c6ca4fd386edazCgVXjsCj7sEOSiBXk7KyKxd4RKBgVCCNxY2QIE9whNwK7XaLJjSeU2⣿':alpha[17], 
             '73b9b3faea927b6b1a94ecda5376b6ab507b202d21755e59b0cf56d5ce04ff0a-wjVLL4NZ7rNkR9WlaJidzN1PkELOOTiaEyTmwDwaD4sBk0voU_PU3w⣿':alpha[18], 
             '235f39325a9dbc7648822ce6c3dc214810416fb55020bbc4e09d2d734e13219c68k3cJJZhi8CNeFsOas7749Z7LgWwXY_Cog1KQjmWRJXy87foj1VG24⣿':alpha[19], 
             'g8454bf91ffae1b0876839ca5846384049ca6eb9c3af666d16fef94d4f5b3ca7b_Av9nEB_1YyVoepsr0nIRjvE6-l9hdXmZz4LUjcf2ECS8P4fdT4luw⣿':alpha[20], 
             'AAB23c538104a7963f5d1bb9da037f9935c42f1fa2f8c8ddb1fe7b5ef605400ab79piiHdp7tAjlzvI5I9fkt3szt17rftUXggc3KkYEf5YBO2J48BLep⣿':alpha[21], 
             'B63c23da0f9ab3e600a1393e71fb87d48603ce08cf1c0e34468e6f4216878e2d8FU_9eohS6XH_REfuhS7n5BlrJdDM2kfLnYB9gw_oB2SBdhas1qRQEQ⣿':alpha[22], 
             '95bc603278dea260cd0612ff9865b0908cb330c6ddb4b17832313a738433df17NM4J6gerzkQAWEDV93tawPJ9eY7zII-DuJ8HQM7Ljk3LLnVMU4IXf60⣿':alpha[23], 
             '7dbed888e53e09e4ea0946f0687654f6b986f20842cb49e8cfc43fcecdb168d3NuESGJ_0stMrkHzvRgeeK0GKyG0_OFeCzE3Ed9oyEg-WRoKKNWYu-G4⣿':alpha[24], 
             '239a2c66ea0b7bcf8b3d157a4a950bbce090700731941eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHCW6iGKP3qL6qkqadXD⣿':alpha[25],
             '048ed5a32944e0cf9124bbfdc4d2c39fc03b3aa59dad85ddc3e53c2e3739ab9a58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHCW6⣿':alpha[26],
             'dfc77c639b0820da9d3e80d8db6bea4bb46683b4d4ead6b8d70b6f70d6ae4b96ee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHC⣿':alpha[27],
             '1Ctfrhv2HHFMpBRJSYB3ACvtq15gYv1Ths741eaee51Cw3BiJ6KJyrwj9u9t7rhxtgJd7bSFX4Av8c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0Lsy⣿':alpha[28],
             'af33bf07421df8947ffb8789e103f1433b49925411738d2d7c5e0d5cd611277c6d741eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqR⣿':alpha[29],
             'bea53353a314db32f93335017f60495ac6e222fd69b1ff87a9def1ec1843c6461eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHe⣿':alpha[30],
             '008e134f5caf483479da95f20869f86becff97ffd4f97f4b3cf1568668c2244b835408ae2dbd11c265f1b9bf9dde390b11182dfdf6d741eaee58c4f⣿':alpha[31],
             'f21c200b6030e109201b7031cab4ce827d7c0deac8ea621c564a8d524734a8bd35ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1⣿':alpha[32],
             '641c3b28f5347e185ed63f2990b09a2d13dabd99c69ed8d454294464169e2db95ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1R⣿':alpha[33],
             'bf149bf660fadbd4cafd813f57357906cd19de107afc9bc236065c5a18ff76735ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1P⣿':alpha[34],
             '95094a1d7d22fcf0dc70577cf5a8257047bb7fe09d4ad2de814ae170be93ac20416354504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3G97⣿':alpha[35],
             '2cbbeb977464ca8cd9c9fac1c74df63e37aa0c2a1f8a57eedf70b4df976f16744504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3G97Ft129⣿':alpha[36],
             '45a1e02612d9e35e8ff9a5944e98dd15631ed3ffea487b08f1604abd1e28367713635ad615416354504e201182dfdf6d741eaee58c4fd08604814bV⣿':alpha[37],
             '71bdde7634edd97dda6677364373b617ef26e1434a8185b208494bcd83d3188a615416354504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3⣿':alpha[38],
             '4c392e0f2cefbfc16ed649b176bd8d277cdcc5d8d233c95451bbf362f46198aa15416354504e201182dfdf6d741eaee58c4fd08604814bVio1Rmn3G⣿':alpha[39],
             '76873fc39bcfc40723ba8330fe963fc1e3ca1c4441be25c4ef7b1a3cccc292f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bVio1R⣿':alpha[40],
             'e456744a81dc975ed7a0e59df9f5134f9801310671f9793cfaa7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bV⣿':alpha[41],
             '666b246dbc764c19be22279150812ec3941014fd4cc317478d206751564f70f91ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd08⣿':alpha[42],
             'de5ac1306b1719848cf85c93f2b8b6ab3167feadf41066942c116dd4261ef723f5134f9801310671f9793cfaa7011b1ffd80d892f65ad6154163545⣿':alpha[43],
             '0d1e4ab8b251a45b840505d9569c243ecc2705b8911cfd0df29e7655967f35dea7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58⣿':alpha[44],
             '55fd5164acd2e579b0edd90cfbf48f849f1cdaf63a0a0e5ae9a106656ccb8bd55134f9801310671f9793cfaa7011b1ffd80d892f65ad61541635450⣿':alpha[45],
             'ee5683595b2e8dbea62ffe35ac5636302790b95700c86c2e3383cb29d24bcd90faa7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee⣿':alpha[46],
             '43e36bbeab1426f432875067006b63b08c923d6c9f14642a7c699dd5b9168a0f9793cfaa7011b1ffd80d892f65ad615416354504e201182dfdf6d74⣿':alpha[47],
             'f9a79777aea7e77a679932538703fd4e9dcfb173960d3a25c5ce439d67da152e011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4⣿':alpha[48],
             'aed835507db62b44bfbb6c2acd4d79b1dc81e0d36d765d414ee82a7f3f1f0eaf1b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd⣿':alpha[49],
             'da104677df9ba78778195b8b94024ebfe939fb6198611db48a18d3f83ce96e7f7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c⣿':alpha[50],
             '1fbead09f5c5e008febb8af9a6613df35e154d26dfa9a79821b3eb489a7a7b79fd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd0860⣿':alpha[51],
             '073e733b151e486400c803835605c0dc0b34bd717df6d8f81e0f6c19f04bfbf21ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd08⣿':alpha[52],
             '368eed2e91d916297c4efa7d1aa6be2b2fb4d4a4ddae142fef1b1c43b52effb00d892f65ad615416354504e201182dfdf6d741eaee58c4fd0860409⣿':alpha[53],
             '3804fe5f96182ec5f98e563e25aa518c001a8491ff70899ccfa060a170f842d3d615416354504e201182dfdf6d741eaee58c4fd08604814bV010125⣿':alpha[54],
             '9de8da0d7e8a97789a23ed1f52d7b4414f02d5297221724c7f279349b7a3ccb780d892f65ad615416354504e201182dfdf6d741eaee58c4fd086048⣿':alpha[55],
             'a5b43678d1d31dde06d6c435ff5fb3f6b39277a59628b5ca553eabb9b198c876f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bV01⣿':alpha[56],
             '7fd3ecee53a2f701a05f5c489b80a8c57a13a706992cbf14e7b937a500b414121b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4fd⣿':alpha[57],
             '786b04f6e34a2fd21b3aae2f94889864025d008025a365b6733680a707ef76b5f65ad615416354504e201182dfdf6d741eaee58c4fd08604814bV01⣿':alpha[58],
             '9c3dcd25fe4acf53a3b1b3d9575b458145fd7189ff1e61a052a7ece74bd2799a0d892f65ad615416354504e201182dfdf6d741eaee58c4fd0860481⣿':alpha[59],
             '6cc5129e82a9c39868660dfbcf7905b8d8d47d452b97bf41303ffdedb8d6b642aa7011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee5⣿':alpha[60],
             'cef322fc485203c7a6fd23088e4cf8ddc703b24a6b1799ea2a8f7d510d06f0c3011b1ffd80d892f65ad615416354504e201182dfdf6d741eaee58c4⣿':alpha[61],
             '841e8cd86a7a643906fe4f082ddd094c85503dfc3652d01d8a0bb97732d05295b87216b3330a780794d1680d892f65ad615416354504e201182dfdf⣿':alpha[62],
             'e74f24ec2afdae83f2bafda4fea5ca893bfc21ee614a148e3286106c2d210394d1680d892f65ad615416354504e201182dfdf6d741eaee58c4fd086⣿':alpha[63],
             '3fa8ed81b79e8905990e7123813401dc2c199e0e29a999aadee67e44ac0e2ed687216b3330a780794d1680d892f65ad615416354504e201182dfdf6⣿':alpha[64],
             'f1b94fd3af2d764ae4277470e822acba347b56d8bdbfbdf50519c0717c3879106fb87216b3330a780794d1680d892f65ad615416354504e201182df⣿':alpha[65],
             '37bf6c9cea9307bf8933501bc4eac7935161686f269d9bd02c6e14b0b599414930a780794d1680d892f65ad615416354504e201182dfdf6d741eaee⣿':alpha[66],
             '67dfcf9f6169aacd59ce47d9744ec2b6f8b1a29727681f0d818c75abcb51b6a9330a780794d1680d892f65ad615416354504e201182dfdf6d741eae⣿':alpha[67],
             '8e3486aaf3aa840f90ea0ebe9c9908f720f4bde6c51ac4d170c8f29b0228596d330a780794d1680d892f65ad615416354504e201182dfdf6d741eao⣿':alpha[68],
             '67286991c9ffda7f718ef5120c091d45b5fb1e143671821e4c07d84a97c5eacda780794d1680d892f65ad615416354504e201182dfdf6d741eaee51⣿':alpha[69],
             'fa5f665dae68d1a93f3366dc3b94de6e80b945ac5bd0e034dc84df805427d95b6b3330a780794d1680d892f65ad615416354504e201182dfdf6d741⣿':alpha[70],
             '771db49534bbde8fa5b7495fe3d99a2ee7659e503b7fdbc1115a981c6f0603b03330a780794d1680d892f65ad615416354504e201182dfdf6d741e1⣿':alpha[71],
             '18188db49534bbde8fa5b7495fe3d99a2ee7659e503b7fdbc1115a981c6f0603b03330a780794d1680d892f65ad615416354504e201182dfdf6d741⣿':alpha[72],
            
             }
    """
    key_codes = list(codes.keys())
    """
    isEmpty=False
    amount2=""
    for i in range(len(amount)):
        if amount[i]!=' ':
            isEmpty=True
        if isEmpty:
            amount2+=amount[i]
            
        
    keys = amount2.split('⣿')
    
    dec=""
    for i in range(len(keys)):
        
        try:
            data = codes[keys[i]+"⣿"]
            dec+=data
        except:
            temp = keys[i]
            keys[i] = keys[i].replace(' ','')
            
            try:
                data = codes[keys[i]+"⣿"]
                dec+=" "+data
            except:
                dec+=temp
    
     
     
    return dec   

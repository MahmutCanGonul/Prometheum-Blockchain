def Cryptograpghy():
    alphabets = string.ascii_letters 
    alpha = []
    result=""
    for i in range(len(alphabets)):
        result = ""+alphabets[i]
        if result.isupper():
            break
        else:
            alpha.append(alphabets[i])
            
    print(alpha)
    codes = {'1ANk1EeLjUbw29vzfzfvZjb7frThog8EpqwehVP0X08QQVWwPY6fWNYFJRiq_ju9954MLGXozaa14jTBKUM6sek_cGaYLKsq7zTIykSEuDwEaI0Y0jhP6Vg':alpha[0],
              'L2ZpJ4rSNPWGgAqRavUv4ZCJTUM5uDbCpLABB3m3SrskVkTehd4GNMP6AvSaMpkepq7QnuPRPCNDZiEiiraf7o1NLvodC5tsVk-kSdaIpNADIJvGCrtvvzZjHey30sY-jYQGegEZaM-Q02533d96cd52baee7a0176039170fdbdeb3fd49437541e75926d9037b1f7196fa2':alpha[1], 
              '1y8kVM47RuhRGfqaJovngFWKMDw8UvwMiQ8ScPmM3XwGUtnzk9PoNrYCj-Y3RRwDjrwwBi8hF52WitkaJXOfVFHvv-c6XZjmKNurxwMB-5Qx9pIRUXVsXi7vZ7tOTfYBKW4KKn86g02a1b365543eb00e7438cc2b875b2e6d2060b44f2354b41ec4d3792cbed4cb44d8':alpha[2],
              'KwrFuz3ETNcacYnt99AaoP64HbTkzJzg81TehLHtDqqM3iR6hCVjNMd0aZP80zepGDpYkIkS3O-iDT2MPTm_8_JpEMOFLQBfqSfPWqkD_KUAKJPsM8UrfdMZm6UAZqBleIwYEn7q2g02c32205f3435a001f8f849632599ef5518f9ee078d47be8952bf1efa75005453d':alpha[3],
              'b9091ec7b189de122b73291625c4d2a6c723bb76a87043e4723e9a679e0fae30Munf-pmmM_wMgQN2ltqE49C5U1jUK0pg3rPqF9cy5Xk83xV6KTiH3jW6tEwknhZhKiYmjFfBVg611GMkOTv2YSA036599bda1b8fa5f092ac82040eda8e709610c0d99a2fb4def8914b070edda5ec4':alpha[4], 
              'a112f18140b79efd2e95342fc308ad1140b4080d6fef74affc1f281f39427f56QImixVAxGm0d6vdynL71xVMUchuQ0_IOSIVWGYWl0fvyDQKq4lB2K-k5wpqXPUURaC8iTarQU11WL4_Q82Xg027168632f134cdc5e5a6473aadc95fec5b5904e29c7d2b20a688a5225818dc99b':alpha[5], 
              '8d057ac3a67e6714183e778d1cb02d32085cce244088725b7fde552e1459a8edgJfx6DFue2Y19BMe5puBGLpVcVCvZXUYynU-OAPWNNzvghRhtPej9x7_WSmswDJZ1g4ErQ3alH360q6Nlwrgx1':alpha[6], 
              '93bc19abdc36c50be13e1b8e2302d6bad0626c0d5a480678c9592c6febfb751c_J14VyLkPo0IPQaogBarFUaPDrMDJaWQjWlv0Nh2zvZWJgT2TZEU0_9GYWYEenxZh2loufTVnG0fD44NKp5jQtg':alpha[7], 
              '73bf6f9631ab2543900f5ed1a3d89dd920f0493b5f4b3ffbce98c0bd99dceb20-f9xvnkAY5qY2xNJU0T81xpaIO-5_GAWApph3rus_-hZI-kfPVMZ7c9UZKCvNY_29_LoICP-igRoz2vDzHnslwsasa':alpha[8], 
              'eaec26a596e586e4bed164c1c8dddfaec6d3ca7d6a22115f1d9783923b225d788iGIaMQSch8Hc3cI7RQHtOx0EADIilyUzXcQDtMXchwNgRaZnqED_QEPigU2kaOaCqP2tK4rN2sWL7x-at8Aopwe':alpha[9], 
              '7741724df098c0827cb84c5811dfa6297e6edd7db99e7ba73e5b41e3b3e0bc99h4PyPoNMsercOGqkMZScAZV2UnJQLNgRvGg2InLYQk7vfJaKMHf1dhM2Jh8narnwfeW1PXGxZJUvj8QxKMQrEA0224ab09ac86a0159566f270a3dc13823a3c0858426b35fc45c4d69346576761c6':alpha[10], 
              '422e773929235813e0a62b09d9f9c0c4f22aecf1839ff47f6fcc98f11183adc0ZNGvJsvRmI2zfD8aoUa3OLgjMjAwESVPxU7e_kMQTHLpevt7mNUvTZpSBapyaXEx0IvFwRXdEN3q3SYeuM-g02ef902b7cd87aa8a30ede9ae022253c43d96c7afbd9a5122dff3f6b3fc77fbeda':alpha[11], 
              '0c0082dcbfea0f96b70f25762cc530926284c5aff65c5d0bd405e613a921f56eMyCsOPDtlQOV-sXjplhfWO561BBel0_qBNyhrMyYK-S0QLsct9oQyqBmMJKXK_wFus5PigZLkmtfgFg9Ih_VA0385a358f693ef76f20a5080020f37bc3360b380ee396226308df55e21e70dad50':alpha[12], 
              'd5a30cbb6e3a06bbf02c428e0575802150b6b10437f2d5c2cfa5b60e5ba1d965Vocp8NrL1YH9AkN2rIvNfOysNQ2cCEMlFRmLP4tsvrwAPwJ8J-J-m_O_CA0jZ7JGT3pxoYWTayuS0VO4mepg022735f81ef9cf35ab9f9b9d7c7c39338d737e57c96b55ddb59aae5b2cc2bb25e6':alpha[13], 
              '1708625668a5c44184770358ad32b41a5ebec93bde3eaeba87b700e017b68305V0hVGo1WCJPyuWpOZ4gX2ddgl8EKdMlzwZVDGZiIN6G_E8mz2-2fA8GIvdH3kCe4xqMzY-QDeQosNVqnikH78w==':alpha[14], 
              '7078e2646f024b4ee0c291c4f94ee5bd3f4aa1ba3b7e4db3b364631fd7259571pkPwUXo7uGwBIq6IrtoP-PgfD_FF-Vl321WCXDs_imyuZYRpK9AI1Dvc-A3G379inT0u_zOAR2ZzgWwuk0uw??assetdhe':alpha[15], 
              '4fbccd467afcc8508e1b1249f8358e357ba354201a105d208b28fddbd01022daoaj1ckkYzgEEH9X9H-51Rea4ooxy-A2ScGYLDE-Aqfjrns2Rg_KSdM_Vlia2iOvuI9VvqP9JqSZ8c1ODznOMg0304735b762278b5c0e35e42e9df66c368df7accee5ef116e1fb2bb7b0380bd037':alpha[16], 
              '97a115722a2cb052e7b27351f568b452d465de1c4cb994d3d52c6ca4fd386edazCgVXjsCj7sEOSiBXk7KyKxd4RKBgVCCNxY2QIE9whNwK7XaLJjSeU2HF0nKjzDt9xGRUCrG1JxXzSSe72-EQ02977745f1dd57e44e715ba777e4b704c4c4b7dfbaf29b9874cd85a4a91732e7ea':alpha[17], 
              '73b9b3faea927b6b1a94ecda5376b6ab507b202d21755e59b0cf56d5ce04ff0a-wjVLL4NZ7rNkR9WlaJidzN1PkELOOTiaEyTmwDwaD4sBk0voU_PU3wcKC26whsD5N0RPyF4hRCRPDJJBvdsLw03f85d960112923b317828f4ed3b2d18a5d9bddb501f51f5864f6f62fe1f89b6ec':alpha[18], 
              '235f39325a9dbc7648822ce6c3dc214810416fb55020bbc4e09d2d734e13219c68k3cJJZhi8CNeFsOas7749Z7LgWwXY_Cog1KQjmWRJXy87foj1VG24lE2MJV3VuyvNUKa90xQOvgHYUVg024bf604112d7275c285670227a356c08bc51d05df730fcaa8bd52602336c1a417':alpha[19], 
              'g8454bf91ffae1b0876839ca5846384049ca6eb9c3af666d16fef94d4f5b3ca7b_Av9nEB_1YyVoepsr0nIRjvE6-l9hdXmZz4LUjcf2ECS8P4fdT4luRL-Q5alcKg9SF3jFUKj3gwAByl3p77A1KyXCQjAhzr9UJfCiath6sBmxdkLo1c71B':alpha[20], 
              'AAB23c538104a7963f5d1bb9da037f9935c42f1fa2f8c8ddb1fe7b5ef605400ab79piiHdp7tAjlzvI5I9fkt3szt17rftUXggc3KkYEf5YBO2J48BLeUJNrxg-K_wI9yFgqTNwe__sVfTcUHLkMsg03d731dbb23ee908cc301d0a71dc918c12928d61decb5c9978d2b0f4389947b432':alpha[21], 
              'B63c23da0f9ab3e600a1393e71fb87d48603ce08cf1c0e34468e6f4216878e2d8FU_9eohS6XH_REfuhS7n5BlrJdDM2kfLnYB9gw_oB2SBdhas1qRQEQkw6d-x-WFD_MfflVRa6maL1wCkvk5ga4efff66f64667ff4ec62643655bf1285f269533c6e13e675a38a08f663d2202':alpha[22], 
              '95bc603278dea260cd0612ff9865b0908cb330c6ddb4b17832313a738433df17NM4J6gerzkQAWEDV93tawPJ9eY7zII-DuJ8HQM7Ljk3LLnVMU4IXf607rC1AwM7wZ_I_1cM72pysw-LuM0QoUDSQ1KBkAyzt21fWJT9VFMq52567iHfo7nZuHZ':alpha[23], 
              '7dbed888e53e09e4ea0946f0687654f6b986f20842cb49e8cfc43fcecdb168d3NuESGJ_0stMrkHzvRgeeK0GKyG0_OFeCzE3Ed9oyEg-WRoKKNWYu-G4fCW0zDjCxV8CFGTzVE4cTgA92AWd2zg026cc6b89de234225be55dd9f1207723d62b8b53288090f592be393dcda76c0bdf':alpha[24], 
              '239a2c66ea0b7bcf8b3d157a4a950bbce090700731941eaee58c4fd08604814bVio1Rmn3G97FtGM08vDxXV-o-0LsyqRePHenHCW6iGKP3qL6qkqadXDDwXL_O_xXpqGZVwO0sQXwpI0az6eQ1LNii4wYNysFozYCFD9qGu1cP2trJhNwiB':alpha[25]}
    
    key_codes = list(codes.keys())
    message = "I wanna ask you something about how did you learn this techniq????"
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
    
    
    print(enc)
    dec=""
    for i in range(len(decs)):
        try:
            dec+=codes[decs[i]]
        except:
            dec+=decs[i]
            
             
    
    print(dec)

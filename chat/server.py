import datetime

# now = datetime.datetime.now()
# x = str(now.strftime("%Y-%m-%d %H:%M:%S"))

# y = datetime.datetime(2022,12,1,1,0,0)

def finddiff(curr,past):
    # print(x)
    # print(y)
    a = curr-past

    seconds = a.seconds
    mins = a.total_seconds()//60
    hours = a.total_seconds()//3600
    days = a.days
    months = days//30
    years= months//12
    return [seconds,mins,hours,days,months,years]


# #print(a.months)
# print(a.seconds)
# print("total seconds are ",a.total_seconds())
# print("mins",int(round(a.total_seconds()/60, 0)))
# if(years==0):
#     if months!=0:
#         if(months<=1) :  print(months,"month ago")
#         else : print(months,"months ago")
#     else:
#         if days!=0:
#             if(days<=1) :  print(days,"day ago")
#             else : print(days,"days ago")
#         else:
#             if hours!=0:
#                 if(hours<=1) :  print(hours,"hour ago")
#                 else : print(hours,"hours ago")
#             else:
#                 if mins!=0:
#                     if(mins<=1) :  print(mins,"min ago")
#                     else : print(mins,"mins ago")
#                 else:
#                     if seconds!=0:
#                         if(seconds<=1) :  print(seconds,"second ago")
#                         else : print(seconds,"seconds ago")
# else:
#     if(years<=1) :  print(years,"year ago")
#     else : print(years,"years ago")
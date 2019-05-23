import cs_hanyang_parser
import cs_hanyang_db

def crawling():
        board_zip = cs_hanyang_parser.crawl()
        
        return board_zip

def check_update():
        board_zip = crawling()
        
        cs_hanyang_db.use_db()
        latest = cs_hanyang_db.get_latest()
        cnt = 0
        add_list = []
        for(number, title, date) in board_zip:
                if(int(latest[2]) < date):
                        print("Number : " + number + " Title : " + title + " Date : " + str(date))
                        cnt += 1
                        cs_hanyang_db.insert(number,title,date)
                        new_list = [number,title,date]
                        add_list.append(new_list)

        cs_hanyang_db.commit()
        cs_hanyang_db.close()
        if(cnt) :
                for (number,title,date) in add_list:
                        print("Number: " + number + " Title: " + title + " Date: " + str(date))
                print(str(cnt)+ " records updated")
        else :
                print("No new articles")
        

def main():
        # update()
        check_update()

if __name__ == "__main__":
    main()

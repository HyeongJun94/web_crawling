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
                if(latest[2] < date):
                        cnt += 1
                        cs_hanyang_db.insert(number,title,date)
                else:
                        break
        cs_hanyang_db.commit()
        cs_hanyang_db.close()
        print(str(cnt)+ " records updated")

def main():
        # update()
        check_update()

if __name__ == "__main__":
    main()

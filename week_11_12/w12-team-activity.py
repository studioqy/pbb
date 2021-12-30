# 12/3 W12 Team Activity
most_chapters = 0
least_chapters = 999
ot_chapters = 0
nt_chapters = 0
pogp_chapters = 0
dnc_chapters = 0
bom_chapters = 0
bom_most_chapters = 0
chosen_most_chapters = 0

chosen_scripture = input(
    "Which volume of scripture would you like to learn the most about?")

with open("books_and_chapters.txt") as books_and_chapters:
    for single_line in books_and_chapters:
        single_phrase = single_line.split(":")
        book = single_phrase[0]
        chapters = int(single_phrase[1])
        scripture = single_phrase[2]
        scripture = scripture.rstrip()
        if scripture == "Book of Mormon":
            print(f"Scripture: {scripture} Book: {book} Chapters: {chapters}")
            if chapters > bom_most_chapters:
                bom_most_chapters = chapters
                bom_most_book = book
        if scripture == chosen_scripture:
            if chapters > chosen_most_chapters:
                chosen_most_chapters = chapters
                chosen_most_book = book
        if chapters > most_chapters:
            most_chapters = chapters
            most_book = book
            most_scripture = scripture
        if scripture == "Old Testament":
            ot_chapters += chapters
        elif scripture == "New Testament":
            nt_chapters += chapters
        elif scripture == "Pearl of Great Price":
            pogp_chapters += chapters
        elif scripture == "Doctrine and Covenants":
            dnc_chapters += chapters
        elif scripture == "Book of Mormon":
            bom_chapters += chapters
    print(
        f"The Book with the most chapters is {most_book} with {most_chapters} chapters in {most_scripture}")
    print(
        f"The Book in the Book of Mormon with the most chapters is {bom_most_book} with {bom_most_chapters} chapters")
    print(
        f"The Book in the {chosen_scripture} with the most chapters is {chosen_most_book} with {chosen_most_chapters} chapters")

    if ot_chapters > nt_chapters and ot_chapters > pogp_chapters and ot_chapters > dnc_chapters and ot_chapters > bom_chapters:
        book_most_chapters = "Old Testament"
    elif nt_chapters > ot_chapters and nt_chapters > pogp_chapters and nt_chapters > dnc_chapters and nt_chapters > bom_chapters:
        book_most_chapters = "New Testament"
    elif pogp_chapters > ot_chapters and pogp_chapters > nt_chapters and pogp_chapters > dnc_chapters and pogp_chapters > bom_chapters:
        book_most_chapters = "Pearl of Great Price"
    elif dnc_chapters > ot_chapters and dnc_chapters > nt_chapters and dnc_chapters > pogp_chapters and dnc_chapters > bom_chapters:
        book_most_chapters = "Doctrine and Covenants"
    elif bom_chapters > ot_chapters and bom_chapters > nt_chapters and bom_chapters > pogp_chapters and bom_chapters > dnc_chapters:
        book_most_chapters = "Book of Mormon"
    print(f"The Scripture with the most chapters is the {book_most_chapters}")

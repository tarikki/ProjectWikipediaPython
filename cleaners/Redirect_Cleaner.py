__author__ = 'extradikke'

if __name__ == '__main__':

    with open("/media/extradikke/FastFiles/wikidata/articles_processed_try.txt", mode="r") as pages, open(
            "/media/extradikke/FastFiles/wikidata/articles_processed_no_redirects.txt", mode='w') as destination, open(
            "/media/extradikke/FastFiles/wikidata/redirects_try.txt", mode='r') as file_redirects:
        redirects = dict()
        counter = 0
        c_redirects = 0
        c_healthy_links = 0
        rd_error_counter = 0
        for line in file_redirects:
            try:
                key, value = line.split("|")
                redirects[key.lower().strip()] = value.lower().strip()
            except ValueError:
                rd_error_counter += 1
                # print(line)
        print("%d faulty redirect lines" % rd_error_counter)
        for line in pages:
            counter += 1
            clean_links = []
            all_links = [link.lower().strip() for link in line.split("|")]
            clean_links.append(all_links[0])
            for link in all_links[1::]:
                if link in redirects:
                    c_redirects += 1
                    clean_links.append(redirects.get(link))
                else:
                    c_healthy_links += 1
                    clean_links.append(link)

            destination.write("|".join(clean_links)+"\n")
            if counter % 100000 == 0:
                print("%d pages processed, %d redirects fixed, percentage of links fixed %.2f" % (
                counter, c_redirects, 100*c_redirects / (c_redirects + c_healthy_links)))
        print("%d pages processed, %d redirects fixed, percentage of links fixed %.2f" % (
                counter, c_redirects, 100*c_redirects / (c_redirects + c_healthy_links)))

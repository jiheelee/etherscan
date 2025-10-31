def safe_get_text(cell):
    try:
        if cell.find("span", title=True):
            return cell.find("span")["title"]
        return cell.text.strip()
    except:
        return cell.text.strip()

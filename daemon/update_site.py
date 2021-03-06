import compose
import db
import nginx


def get_website_info(website_id):
    with db.open_db() as conn:
        with conn.cursor() as cur:
            query = "SELECT domain,use_https,db_password,files_password,version FROM users_website WHERE id=%s"
            cur.execute(query, (website_id,))
            data = cur.fetchone()
            return data


def run(website_id):
    (domain, use_https, db_password, files_password, version) = get_website_info(website_id)

    compose.install(website_id, domain, use_https, db_password, files_password, version)
    nginx.install(website_id, domain, use_https)

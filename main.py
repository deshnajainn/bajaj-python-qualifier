import requests

def main():
    webhook_url = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"
    access_token = "eyJhbGciOiJIUzI1NiJ9.eyJyZWdObyI6IjUyOCIsIm5hbWUiOiJEZXNobmEgSmFpbiIsImVtYWlsIjoiZGVzaG5hamFpbjIyMTIxMUBhY3JvcG9saXMuaW4iLCJzdWIiOiJ3ZWJob29rLXVzZXIiLCJpYXQiOjE3NDY5NjI3NjUsImV4cCI6MTc0Njk2MzY2NX0.czXHFkbWGP8E1vtIlPywsS5gujC03Q298kVl0o_toy"

    final_sql = {
        "finalQuery": """
        SELECT 
            e1.EMP_ID,
            e1.FIRST_NAME,
            e1.LAST_NAME,
            d.DEPARTMENT_NAME,
            COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
        FROM EMPLOYEE e1
        JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
        LEFT JOIN EMPLOYEE e2 
            ON e1.DEPARTMENT = e2.DEPARTMENT 
            AND e1.DOB > e2.DOB
        GROUP BY 
            e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
        ORDER BY e1.EMP_ID DESC;
        """
    }

    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, json=final_sql, headers=headers)

    if response.status_code == 200:
        print("✅ Submission successful!")
    else:
        print("❌ Submission failed:", response.text)

if __name__ == "__main__":
    main()

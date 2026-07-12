from flask import Blueprint,request,jsonify
from models import db,Issue

issue_bp=Blueprint("issue_bp",__name__)

@issue_bp.route("/issues",methods=["GET"])
#to return issues
def get_issue():
    issues=Issue.query.all()

    results=[]
    for issue in issues:
        results.append({
            "id":issue.id,
            "title":issue.title,
            "description":issue.description,
            "Priority":issue.priority,
            "status":issue.status,
            "assigned_to":issue.assigned_to,
            "created_date":issue.created_data
        })
    return jsonify(results)



@issue_bp.route("/issues",methods=["POST"])
 #to create new issues
def create_issue():
   data=request.get_json()
   issue=Issue(
      title=data["title"],
      description=data["description"],
      priority=data["priority"],
      assigned_to=data["assigned_to"]
   )
   db.session.add(issue)
   db.session.commit()
   return jsonify({
      "message":"issue created successfully"
   }),201
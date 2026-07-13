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


@issue_bp.route("/issues/<int:id>",methods=["PUT"])
def update_issue(id):
    #to update an existing issue.
    issue=Issue.query.get_or_404(id)

    data=request.get_json()

    issue.title=data.get("title",issue.title)
    issue.description=data.get("description",issue.description)
    issue.priority=data.get("priority",issue.priority)
    issue.status=data.get("status",issue.status)
    issue.assigned_to=data.get("assigned_to",issue.assigned_to)

    db.session.commit()

    return jsonify({
        "message":"issue updated"
    })



@issue_bp.route("/issues/<int:id>",methods=["DELETE"])
def delete_issue(id):
    #to delete  an issue
    issue=Issue.query.get_or_404(id)

    db.session.delete(issue)
    db.session.commit()

    return jsonify({
        "message":"Issue deleted successfully"
    })



@issue_bp.route("/issues/status/<string:status>",methods=["GET"])
def get_issues_by_status(status):
    #issues filtered by status
    issues=Issue.query.filter_by(status=status).all()
    results=[]

    for issue in issues:
        results.append({
            "id":issue.id,
            "title":issue.title,
            "description":issue.description,
            "priority":issue.priority,
            "status":issue.status,
            "assigned_to":issue.assigned_to,
            "created_date":issue.created_data
        })

    return jsonify(results)


@issue_bp.route("/issues/priority/<string:priority>", methods=["GET"])
def get_issues_by_priority(priority):
    #to return issues by filtered by priority
    issues=Issue.query.filter_by(priority=priority).all()
    results=[]
    for issue in issues:
        results.append({
        "id":issue.id,
        "title":issue.title,
        "description":issue.description,
        "priority":issue.priority,
        "status":issue.status,
        "assigned_to":issue.assigned_to,
        "created_date":issue.created_data
        

        })
    return jsonify(results)


      

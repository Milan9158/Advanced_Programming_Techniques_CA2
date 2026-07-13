from flask import Blueprint,jsonify
from models import Issue,Vulnerability

report_bp=Blueprint("report_bp",__name__)

@report_bp.route("/reports/issues",methods=["GET"])
def issue_report():
    #return summary of issues

    total=Issue.query.count()
    open_issues=Issue.query.filter_by(status="open").count()
    closed_issues=Issue.query.filter_by(status="closed").count()

    return jsonify({
        "total_issues":total,
        "open_issues":open_issues,
        "closed_issues":closed_issues
    })


@report_bp.route("/reports/vulnerabilities",methods=["GET"])
def vulnerability_report():
    #return summary of vulnerabilties
    total=Vulnerability.query.count()
    open_vulnerabilities=Vulnerability.query.filter_by(status="Open").count()
    closed_vulnerabilities=Vulnerability.query.filter_by(status="Closed").count()

    return jsonify({
        "total_vulnerabilities":total,
        "open_vulnerabilities":open_vulnerabilities,
        "closed_vulnerabilities":closed_vulnerabilities
    })
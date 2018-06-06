package in.co.dhrubaray.spark.core.beans;

import java.io.Serializable;

public class Student implements Serializable {
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private int studentId;
	private String name;
	private String department;
	private String subject;
	private int marks;
	
	public Student() {
		super();
	}
	
	public Student(int studentId, String name, String department, String subject, int marks) {
		super();
		this.studentId = studentId;
		this.name = name;
		this.department = department;
		this.subject = subject;
		this.marks = marks;
	}
	public int getStudentId() {
		return studentId;
	}
	public void setStudentId(int studentId) {
		this.studentId = studentId;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getDepartment() {
		return department;
	}
	public void setDepartment(String department) {
		this.department = department;
	}
	public String getSubject() {
		return subject;
	}
	public void setSubject(String subject) {
		this.subject = subject;
	}
	public int getMarks() {
		return marks;
	}
	public void setMarks(int marks) {
		this.marks = marks;
	}
}

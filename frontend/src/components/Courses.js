import { useState, useEffect } from 'react';

function Courses() {
  const [courses, setCourses] = useState([]);
  
  useEffect(() => {
    fetch('http://localhost:5000/api/courses')  // For Flask
    // OR
    // fetch('http://localhost:8000/api/courses/') // For Django
      .then(response => response.json())
      .then(data => setCourses(data))
      .catch(error => console.error('Error fetching courses:', error));
  }, []);

  return (
    <div>
      <h2>Our Courses</h2>
      <div className="courses-container">
        {courses.map(course => (
          <div key={course._id || course.id} className="course-card">
            <h3>{course.name}</h3>
            <p>{course.description}</p>
            <p>Price: ${course.price}</p>
            <p>Duration: {course.duration} minutes</p>
            <p>Difficulty: {course.difficulty}</p>
            <button>Book Now</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Courses;

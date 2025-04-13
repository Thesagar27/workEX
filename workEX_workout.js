document.addEventListener("DOMContentLoaded", function () {
  const videoGrid = document.querySelector(".video-grid");

  const workouts = [
    {
      title: "Full Body Burn 🔥",
      videoUrl: "https://www.youtube.com/embed/50kH47ZztHs"
    },
    {
      title: "10 Min Abs 💪",
      videoUrl: "https://www.youtube.com/embed/hxjKZcOT17E" // Chloe Ting - works perfectly
    },
    {
      title: "Beginner Yoga 🧘‍♀️",
      videoUrl: "https://www.youtube.com/embed/v7AYKMP6rOE"
    },
    {
      title: "Stretch Routine 🙆",
      videoUrl: "https://www.youtube.com/embed/I9nG-G4B5Bs" // Well+Good: gentle full body
    },
    {
      title: "Low Impact HIIT 💥",
      videoUrl: "https://www.youtube.com/embed/qHQ_E-f5278" // Heather Robertson - verified
    },
    {
      title: "Fat Burn Cardio 🏃‍♂️",
      videoUrl: "https://www.youtube.com/embed/ml6cT4AZdqI"
    }
  ];

  videoGrid.innerHTML = "";

  workouts.forEach(workout => {
    const card = document.createElement("div");
    card.className = "video-card";
    card.innerHTML = `
      <h3>${workout.title}</h3>
      <iframe width="100%" height="215" src="${workout.videoUrl}"
        frameborder="0" allow="accelerometer; autoplay; clipboard-write;
        encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    `;
    videoGrid.appendChild(card);
  });
});

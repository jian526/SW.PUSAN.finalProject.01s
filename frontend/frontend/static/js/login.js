loginBtn.addEventListener("click", async (e) => {
  e.preventDefault();

  const id = usernameInput.value.trim();
  const password = passwordInput.value.trim();
  const loginLink = document.querySelector("a[href='/']");
  loginLink.addEventListener("click", (e) => e.preventDefault());

  if (!id || !password) {
    alert("아이디와 비밀번호를 모두 입력해주세요.");
    return;
  }

  try {
    const res = await fetch("/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      body: new URLSearchParams({ id, password }),
    });

    if (!res.ok) {
      alert("로그인 실패: 아이디 또는 비밀번호가 올바르지 않습니다.");
      return;
    }

    const data = await res.json();
    if (data.success) {
      document.cookie = `user_name=${data.user_name}; path=/`;
      window.location.href = "/index.html";
    } else {
      alert("로그인 실패: 알 수 없는 오류");
    }
  } catch (error) {
    console.error("로그인 요청 오류:", error);
    alert("서버와 연결할 수 없습니다.");
  }
});

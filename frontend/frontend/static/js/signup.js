document.querySelector('.rectangle-parent').addEventListener('click', async () => {
  const username = document.querySelector('input[placeholder="아이디"]').value.trim();
  const password = document.querySelector('input[placeholder="비밀번호"]').value.trim();
  const passwordCheck = document.querySelector('input[placeholder="비밀번호 확인"]').value.trim();
  const codeKey = document.querySelector('input[placeholder="코드번호"]').value.trim();
  const storeName = document.querySelector('input[placeholder="점포명"]').value.trim();
  const ownerName = document.querySelector('input[placeholder="점주명"]').value.trim();
  const phone = document.querySelector('input[placeholder="전화번호"]').value.trim();
  const email = document.querySelector('input[placeholder="이메일"]').value.trim();

  if (!username || !password || !codeKey || !storeName || !ownerName) {
    alert("필수 입력 항목을 모두 입력해 주세요.");
    return;
  }

  if (password !== passwordCheck) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }

  try {
    const res = await fetch("http://localhost:8000/auth/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: new URLSearchParams({
        id: username,
        password: password,
        code_key: codeKey,
        name: ownerName,
        store_name: storeName,
        phone: phone,
        email: email
      })
    });

    const result = await res.json();
    if (res.ok) {
      alert("회원가입이 완료되었습니다!");
      window.location.href = "login.html";
    } else {
      alert(result.detail || "회원가입 실패");
    }
  } catch (error) {
    alert("오류 발생: " + error.message);
  }
});

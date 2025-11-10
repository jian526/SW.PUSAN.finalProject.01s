document.addEventListener("DOMContentLoaded", () => {
  fetch("/cctvs/api/list")
    .then(res => res.json())
    .then(data => {
      // ✅ 메인 카메라가 가장 위로 오도록 정렬
      data.sort((a, b) => (b.is_main ? 1 : 0) - (a.is_main ? 1 : 0));

      document.getElementById("cctv-count").innerText = data.length;

      const container = document.getElementById("cctv-container");
      container.innerHTML = "";

      data.forEach((cctv, index) => {
        const card = document.createElement("div");
        card.className = "overlap-wrapper";
        card.innerHTML = `
          <div class="overlap">
            <div class="xnix-line-video">
              <div class="overlap-2">
                <div class="vector">
                  <div class="overlap-group-2">
                    <img class="vector-2" src="/static/images/cctv${(index % 4) + 1}.svg" />
                  </div>
                </div>
              </div>
            </div>
            ${cctv.is_main ? `<div class="text-wrapper-5">MAIN</div>` : ""}
            <div class="text-wrapper-6">${cctv.name || `카메라 ${index + 1}`}</div>
            <div class="text-wrapper-7">${cctv.location || "-"}</div>
            <div class="text-wrapper-8">${cctv.model || "-"}</div>
            <div class="dropdown-wrapper">
              <img class="more-btn" src="/static/images/Vector.svg" />
              <div class="dropdown-menu hidden">
                <button onclick="editCCTV(${cctv.id})">수정</button>
                <button onclick="deleteCCTV(${cctv.id})">삭제</button>
                <button onclick="setAsMain(${cctv.id})">메인으로 지정</button>
              </div>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    });
});

// ✅ 드롭다운 메뉴 열고 닫기
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("more-btn")) {
    const dropdown = e.target.nextElementSibling;
    document.querySelectorAll(".dropdown-menu").forEach(menu => {
      if (menu !== dropdown) menu.classList.add("hidden");
    });
    dropdown.classList.toggle("hidden");
    e.stopPropagation();
  } else {
    document.querySelectorAll(".dropdown-menu").forEach(menu => {
      menu.classList.add("hidden");
    });
  }
});

// ✅ 기능들
function editCCTV(id) {
  alert(`CCTV ${id} 수정`);
  // TODO: 수정 페이지 연결 or 모달 띄우기
}

function deleteCCTV(id) {
  if (confirm(`정말로 CCTV ${id}를 삭제하시겠습니까?`)) {
    fetch("/cctvs/delete", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: `cctv_id=${id}`
    })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          alert("삭제 완료!");
          location.reload();
        }
      });
  }
}

function setAsMain(id) {
  fetch(`/cctvs/set_main/${id}`, { method: "POST" })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        alert("메인 카메라로 설정되었습니다.");
        location.reload();
      }
    });
}

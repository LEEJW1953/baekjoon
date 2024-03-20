function solution(lines) {
    let answer = 0;
    const times = [];
    for (let i=0; i<lines.length; i++) {
        const [day, time, term] = lines[i].split(' ');
        const date = new Date(day + ' ' + time);
        const dateInt = date.getTime();
        const diff = term.substr(0, term.length-1)*1000 - 1;
        times.push([dateInt - diff, dateInt]);
    }
    for (let i=0; i<times.length; i++) {
        for (let j=0; j<2; j++) {
            let count = 0;
            const start = times[i][j];
            for (let k=0; k<times.length; k++) {
                if (!((times[k][0]>(start+999)) || (times[k][1]<start))) {
                    count++;
                }
            }
            answer = Math.max(answer, count);
        }
    }
    return answer;
}
-- 코드를 작성해주세요
WITH RECURSIVE PARENT AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION
    SELECT B.ID, B.PARENT_ID, (A.GENERATION + 1) AS GENERATION
    FROM ECOLI_DATA B, PARENT A
    WHERE B.PARENT_ID = A.ID
)
SELECT COUNT(*) AS COUNT, GENERATION
FROM PARENT
WHERE ID NOT IN (
    SELECT PARENT_ID
    FROM PARENT
    WHERE PARENT_ID IS NOT NULL
)
GROUP BY GENERATION
ORDER BY GENERATION;
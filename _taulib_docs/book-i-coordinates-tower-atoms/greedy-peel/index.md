---
{
  "projection_kind": "taulib_declaration",
  "title": "greedy_peel",
  "permalink": "/corpus/taulib/docs/book-i-coordinates-tower-atoms/greedy-peel/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::greedy_peel",
  "declaration_slug": "greedy-peel",
  "kind": "def",
  "name": "greedy_peel",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/corpus/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 218,
  "source_line_end": 227,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L218-L227",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.TowerAtoms",
        "url": "/corpus/taulib/docs/book-i-coordinates-tower-atoms/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L218-L227",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Coordinates.TowerAtoms](/corpus/taulib/docs/book-i-coordinates-tower-atoms/)
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L218-L227)
- Source range: L218-L227
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D19d] One-step greedy peel: extract (A, B, C, D) from X ≥ 2.
    Uses A-adic valuation:
    1. A = largest prime divisor of X
    2. v = v_A(X)
    3. C = max c such that A↑↑(c-1) divides v
    4. B = v / A↑↑(C-1)
    5. T = tower_atom(A, B, C), D = X / T -/
```

## Source Excerpt

```lean
def greedy_peel (x : TauIdx) : TauIdx × TauIdx × TauIdx × TauIdx :=
  if x ≤ 1 then (1, 0, 0, x)
  else
    let a := largest_prime_divisor x
    let v := p_adic_val a x
    let c := max_tet_div a v
    let b := v / (tetration a (c - 1))
    let t := tower_atom a b c
    let d := x / t
    (a, b, c, d)
```

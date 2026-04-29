---
{
  "projection_kind": "taulib_declaration",
  "title": "largest_prime_divisor",
  "permalink": "/verify/taulib/docs/book-i-coordinates-tower-atoms/largest-prime-divisor/",
  "summary_short": "`def` declaration in `TauLib.BookI.Coordinates.TowerAtoms`.",
  "declaration_id": "TauLib.BookI.Coordinates.TowerAtoms::largest_prime_divisor",
  "declaration_slug": "largest-prime-divisor",
  "kind": "def",
  "name": "largest_prime_divisor",
  "module_name": "TauLib.BookI.Coordinates.TowerAtoms",
  "module_url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/",
  "source_line_start": 164,
  "source_line_end": 173,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L164-L173",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Coordinates.TowerAtoms",
        "url": "/verify/taulib/docs/book-i-coordinates-tower-atoms/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L164-L173",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookI.Coordinates.TowerAtoms](/verify/taulib/docs/book-i-coordinates-tower-atoms/)
- Source path: [`TauLib/BookI/Coordinates/TowerAtoms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Coordinates/TowerAtoms.lean#L164-L173)
- Source range: L164-L173
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D19d] Largest prime divisor of n (0 for n ≤ 1). -/
```

## Source Excerpt

```lean
def largest_prime_divisor (n : TauIdx) : TauIdx :=
  if n ≤ 1 then 0
  else go n n
where
  go (n d : TauIdx) : TauIdx :=
    if d ≤ 1 then 1
    else if is_prime_bool d && (n % d == 0) then d
    else go n (d - 1)
  termination_by d
  decreasing_by simp_wf; simp only [TauIdx] at *; omega
```

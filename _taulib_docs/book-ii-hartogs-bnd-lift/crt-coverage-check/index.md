---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_coverage_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/crt-coverage-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.BndLift`.",
  "declaration_id": "TauLib.BookII.Hartogs.BndLift::crt_coverage_check",
  "declaration_slug": "crt-coverage-check",
  "kind": "def",
  "name": "crt_coverage_check",
  "module_name": "TauLib.BookII.Hartogs.BndLift",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/",
  "source_line_start": 88,
  "source_line_end": 102,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L88-L102",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.BndLift",
        "url": "/verify/taulib/docs/book-ii-hartogs-bnd-lift/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L88-L102",
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

- Module: [TauLib.BookII.Hartogs.BndLift](/verify/taulib/docs/book-ii-hartogs-bnd-lift/)
- Source path: [`TauLib/BookII/Hartogs/BndLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/BndLift.lean#L88-L102)
- Source range: L88-L102
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- CRT coverage: every pair (a, b) with 0 ≤ a < P_n and 0 ≤ b < p_{n+1}
    is hit by some x in [0, P_{n+1}).
    Check: the number of distinct CRT pairs equals P_n × p_{n+1} = P_{n+1}. -/
```

## Source Excerpt

```lean
def crt_coverage_check (stage : TauIdx) : Bool :=
  let pn := primorial stage
  let p_next := nth_prime (stage + 1)
  let pn1 := primorial (stage + 1)
  if pn1 <= 1 then true
  else
    -- Count distinct CRT pairs for x in [0, P_{n+1})
    let count := go 0 pn1 0
    count == pn * p_next
where
  go (x fuel acc : Nat) : Nat :=
    if fuel = 0 then acc
    else if x >= primorial (stage + 1) then acc
    else go (x + 1) (fuel - 1) (acc + 1)
  termination_by fuel
```

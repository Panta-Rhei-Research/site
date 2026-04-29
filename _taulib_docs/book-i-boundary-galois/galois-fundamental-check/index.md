---
{
  "projection_kind": "taulib_declaration",
  "title": "galois_fundamental_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-galois/galois-fundamental-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Galois`.",
  "declaration_id": "TauLib.BookI.Boundary.Galois::galois_fundamental_check",
  "declaration_slug": "galois-fundamental-check",
  "kind": "def",
  "name": "galois_fundamental_check",
  "module_name": "TauLib.BookI.Boundary.Galois",
  "module_url": "/verify/taulib/docs/book-i-boundary-galois/",
  "source_line_start": 201,
  "source_line_end": 217,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L201-L217",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Galois",
        "url": "/verify/taulib/docs/book-i-boundary-galois/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L201-L217",
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

- Module: [TauLib.BookI.Boundary.Galois](/verify/taulib/docs/book-i-boundary-galois/)
- Source path: [`TauLib/BookI/Boundary/Galois.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L201-L217)
- Source range: L201-L217
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.T49a] Check that every unit generates a valid Galois action:
    preserves addition (as ring endomorphism) and preserves roots of unity
    (as field automorphism on cyclotomic extension). Verified at stage k. -/
```

## Source Excerpt

```lean
def galois_fundamental_check (k : Nat) : Bool :=
  -- The fundamental check: unit group is closed and all units
  -- are additive endomorphisms
  let pk := primorial k
  unit_group_closed_check k &&
  go 1 pk pk
where
  go (a pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else
      let ok := if is_unit_mod a pk then
        let σ : GaloisAut := { stage := k, multiplier := a }
        galois_additive_check σ
      else true
      ok && go (a + 1) pk (fuel - 1)
  termination_by fuel
```

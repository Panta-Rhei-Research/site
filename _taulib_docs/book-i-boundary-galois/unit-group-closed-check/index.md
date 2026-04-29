---
{
  "projection_kind": "taulib_declaration",
  "title": "unit_group_closed_check",
  "permalink": "/verify/taulib/docs/book-i-boundary-galois/unit-group-closed-check/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Galois`.",
  "declaration_id": "TauLib.BookI.Boundary.Galois::unit_group_closed_check",
  "declaration_slug": "unit-group-closed-check",
  "kind": "def",
  "name": "unit_group_closed_check",
  "module_name": "TauLib.BookI.Boundary.Galois",
  "module_url": "/verify/taulib/docs/book-i-boundary-galois/",
  "source_line_start": 165,
  "source_line_end": 182,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L165-L182",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L165-L182",
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
- Source path: [`TauLib/BookI/Boundary/Galois.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Galois.lean#L165-L182)
- Source range: L165-L182
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D95a] Check that the unit group is closed under multiplication mod M_k. -/
```

## Source Excerpt

```lean
def unit_group_closed_check (k : Nat) : Bool :=
  let pk := primorial k
  go 1 pk pk
where
  go (a pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else go_inner a 1 pk pk && go (a + 1) pk (fuel - 1)
  termination_by fuel
  go_inner (a b pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if b >= pk then true
    else
      let ok := if is_unit_mod a pk && is_unit_mod b pk then
        is_unit_mod ((a * b) % pk) pk
      else true
      ok && go_inner a (b + 1) pk (fuel - 1)
  termination_by fuel
```

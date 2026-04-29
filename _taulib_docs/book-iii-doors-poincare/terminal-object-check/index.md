---
{
  "projection_kind": "taulib_declaration",
  "title": "terminal_object_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-poincare/terminal-object-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.Poincare`.",
  "declaration_id": "TauLib.BookIII.Doors.Poincare::terminal_object_check",
  "declaration_slug": "terminal-object-check",
  "kind": "def",
  "name": "terminal_object_check",
  "module_name": "TauLib.BookIII.Doors.Poincare",
  "module_url": "/verify/taulib/docs/book-iii-doors-poincare/",
  "source_line_start": 67,
  "source_line_end": 86,
  "registry_ids": [
    "III.D35"
  ],
  "related_registry_items": [
    {
      "id": "III.D35",
      "title": "Simply Connected in Category τ",
      "url": "/registry/object/III.D35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L67-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.Poincare",
        "url": "/verify/taulib/docs/book-iii-doors-poincare/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L67-L86",
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

- Module: [TauLib.BookIII.Doors.Poincare](/verify/taulib/docs/book-iii-doors-poincare/)
- Source path: [`TauLib/BookIII/Doors/Poincare.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/Poincare.lean#L67-L86)
- Source range: L67-L86
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D35` — Simply Connected in Category τ

## Immediate Comment / Docstring

```lean
/-- [III.D35] Terminal object check: among all τ-spaces at level k with
    trivial fundamental group, the structure is unique up to isomorphism.
    In τ-terms: any two elements with the same CRT residues are equal. -/
```

## Source Excerpt

```lean
def terminal_object_check (bound db : TauIdx) : Bool :=
  go 0 0 1 ((bound + 1) * (bound + 1) * (db + 1))
where
  go (x y k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 0 1 (fuel - 1)
    else if k > db then go x (y + 1) 1 (fuel - 1)
    else
      let pk := primorial k
      if pk == 0 then go x y (k + 1) (fuel - 1)
      else
        let xr := x % pk
        let yr := y % pk
        let res_x := crt_decompose xr k
        let res_y := crt_decompose yr k
        -- Uniqueness: same residues ⟹ same value
        let ok := if res_x == res_y then xr == yr else true
        ok && go x y (k + 1) (fuel - 1)
  termination_by fuel
```

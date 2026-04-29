---
{
  "projection_kind": "taulib_declaration",
  "title": "cauchy_schwarz_exhaustive",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/cauchy-schwarz-exhaustive/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::cauchy_schwarz_exhaustive",
  "declaration_slug": "cauchy-schwarz-exhaustive",
  "kind": "def",
  "name": "cauchy_schwarz_exhaustive",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 114,
  "source_line_end": 130,
  "registry_ids": [
    "II.T53"
  ],
  "related_registry_items": [
    {
      "id": "II.T53",
      "title": "Cauchy-Schwarz Inequality",
      "url": "/registry/object/II.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L114-L130",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L114-L130",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L114-L130)
- Source range: L114-L130
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T53` — Cauchy-Schwarz Inequality

## Immediate Comment / Docstring

```lean
/-- [II.T53] Exhaustive Cauchy-Schwarz check for basis functions at stage k. -/
```

## Source Excerpt

```lean
def cauchy_schwarz_exhaustive (k : Nat) : Bool :=
  let pk := primorial k
  go_f 0 pk pk
where
  go_f (a pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a >= pk then true
    else go_g a 0 pk pk && go_f (a + 1) pk (fuel - 1)
  termination_by fuel
  go_g (a b pk fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if b >= pk then true
    else
      let f : Nat → Int := fun x => if x == a then 1 else 0
      let g : Nat → Int := fun x => if x == b then 1 else 0
      cauchy_schwarz_check f g k && go_g a (b + 1) pk (fuel - 1)
  termination_by fuel
```

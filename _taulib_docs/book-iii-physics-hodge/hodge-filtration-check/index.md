---
{
  "projection_kind": "taulib_declaration",
  "title": "hodge_filtration_check",
  "permalink": "/verify/taulib/docs/book-iii-physics-hodge/hodge-filtration-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Physics.Hodge`.",
  "declaration_id": "TauLib.BookIII.Physics.Hodge::hodge_filtration_check",
  "declaration_slug": "hodge-filtration-check",
  "kind": "def",
  "name": "hodge_filtration_check",
  "module_name": "TauLib.BookIII.Physics.Hodge",
  "module_url": "/verify/taulib/docs/book-iii-physics-hodge/",
  "source_line_start": 178,
  "source_line_end": 205,
  "registry_ids": [
    "III.P19"
  ],
  "related_registry_items": [
    {
      "id": "III.P19",
      "title": "EM Sector Verification",
      "url": "/registry/object/III.P19/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L178-L205",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Physics.Hodge",
        "url": "/verify/taulib/docs/book-iii-physics-hodge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L178-L205",
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

- Module: [TauLib.BookIII.Physics.Hodge](/verify/taulib/docs/book-iii-physics-hodge/)
- Source path: [`TauLib/BookIII/Physics/Hodge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Physics/Hodge.lean#L178-L205)
- Source range: L178-L205
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.P19` — EM Sector Verification

## Immediate Comment / Docstring

```lean
/-- [III.P19] Hodge filtration at level k: B-part ⊂ B+X ⊂ B+C+X.
    Check that the filtration steps are nested. -/
```

## Source Excerpt

```lean
def hodge_filtration_check (db : TauIdx) : Bool :=
  go 1 (db + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > db then true
    else
      let pk := primorial k
      if pk == 0 || pk > 100 then go (k + 1) (fuel - 1)
      else
        check_filtration 0 pk k && go (k + 1) (fuel - 1)
  termination_by fuel
  check_filtration (x pk k : Nat) : Bool :=
    if x >= pk then true
    else
      let nf := boundary_normal_form x k
      -- F₀ = {x : b=0, c=0, x=0} (zero)
      -- F₁ = {x : c=0, x=0} (B-part only)
      -- F₂ = {x : c=0} (B+X parts)
      -- F₃ = full (B+C+X)
      -- Nesting: if b=0 and c=0, then we're in F₁ iff x_part also = 0
      let in_f1 := nf.b_part > 0 && nf.c_part == 0 && nf.x_part == 0
      let in_f2 := nf.c_part == 0
      -- BNF roundtrip: components reconstruct original (non-trivial surjectivity)
      let roundtrip := (nf.b_part + nf.c_part + nf.x_part) % pk == x
      -- Filtration nesting: F₁ ⊂ F₂ (anything in F₁ is in F₂)
      let nested := if in_f1 then in_f2 else true
      roundtrip && nested && check_filtration (x + 1) pk k
```

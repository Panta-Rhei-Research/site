---
{
  "projection_kind": "taulib_declaration",
  "title": "cyl_compat_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/cyl-compat-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.HolImpliesCont`.",
  "declaration_id": "TauLib.BookII.Domains.HolImpliesCont::cyl_compat_check",
  "declaration_slug": "cyl-compat-check",
  "kind": "def",
  "name": "cyl_compat_check",
  "module_name": "TauLib.BookII.Domains.HolImpliesCont",
  "module_url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/",
  "source_line_start": 71,
  "source_line_end": 82,
  "registry_ids": [
    "II.L01"
  ],
  "related_registry_items": [
    {
      "id": "II.L01",
      "title": "Naturality Forces Cylinder Compatibility",
      "url": "/registry/object/II.L01/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L71-L82",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.HolImpliesCont",
        "url": "/verify/taulib/docs/book-ii-domains-hol-implies-cont/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L71-L82",
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

- Module: [TauLib.BookII.Domains.HolImpliesCont](/verify/taulib/docs/book-ii-domains-hol-implies-cont/)
- Source path: [`TauLib/BookII/Domains/HolImpliesCont.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/HolImpliesCont.lean#L71-L82)
- Source range: L71-L82
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L01` — Naturality Forces Cylinder Compatibility

## Immediate Comment / Docstring

```lean
/-- [II.L01] Cylinder compatibility: stage-local functions map
    cylinders to cylinders.
    Check: cylinder_mem k x y → f_k(x) = f_k(y).
    Flat double loop with single fuel counter. -/
```

## Source Excerpt

```lean
def cyl_compat_check (sf : StageFun) (k bound : TauIdx) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (x y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if y > bound then go (x + 1) 2 (fuel - 1)
    else
      let ok := !cylinder_mem k x y ||
        (sf.b_fun x k == sf.b_fun y k && sf.c_fun x k == sf.c_fun y k)
      ok && go x (y + 1) (fuel - 1)
  termination_by fuel
```

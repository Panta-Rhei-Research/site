---
{
  "projection_kind": "taulib_declaration",
  "title": "abc_high_quality_count",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/abc-high-quality-count/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::abc_high_quality_count",
  "declaration_slug": "abc-high-quality-count",
  "kind": "def",
  "name": "abc_high_quality_count",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 106,
  "source_line_end": 121,
  "registry_ids": [
    "III.D109"
  ],
  "related_registry_items": [
    {
      "id": "III.D109",
      "title": "High Quality Count",
      "url": "/registry/object/III.D109/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L106-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCDeep",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L106-L121",
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

- Module: [TauLib.BookIII.Arithmetic.ABCDeep](/verify/taulib/docs/book-iii-arithmetic-abcdeep/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L106-L121)
- Source range: L106-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D109` — High Quality Count

## Immediate Comment / Docstring

```lean
/-- [III.D109] Count coprime triples (a,b,c=a+b) with c ≥ rad(abc).
    These are the triples where quality q ≥ 1. -/
```

## Source Excerpt

```lean
def abc_high_quality_count (bound : Nat) : Nat :=
  go 1 1 0 ((bound + 1) * (bound + 1))
where
  go (a b acc fuel : Nat) : Nat :=
    if fuel = 0 then acc
    else if a > bound then acc
    else if b > bound then go (a + 1) 1 acc (fuel - 1)
    else
      let g := Nat.gcd a b
      let acc' := if g == 1 then
        let c := a + b
        let r := radical (a * b * c)
        if r > 0 && c >= r then acc + 1 else acc
      else acc
      go a (b + 1) acc' (fuel - 1)
  termination_by fuel
```

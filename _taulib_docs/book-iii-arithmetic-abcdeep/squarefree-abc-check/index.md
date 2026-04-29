---
{
  "projection_kind": "taulib_declaration",
  "title": "squarefree_abc_check",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/squarefree-abc-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Arithmetic.ABCDeep`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCDeep::squarefree_abc_check",
  "declaration_slug": "squarefree-abc-check",
  "kind": "def",
  "name": "squarefree_abc_check",
  "module_name": "TauLib.BookIII.Arithmetic.ABCDeep",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcdeep/",
  "source_line_start": 131,
  "source_line_end": 147,
  "registry_ids": [
    "III.D110"
  ],
  "related_registry_items": [
    {
      "id": "III.D110",
      "title": "Squarefree ABC Check",
      "url": "/registry/object/III.D110/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L131-L147",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L131-L147",
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
- Source path: [`TauLib/BookIII/Arithmetic/ABCDeep.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCDeep.lean#L131-L147)
- Source range: L131-L147
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D110` — Squarefree ABC Check

## Immediate Comment / Docstring

```lean
/-- [III.D110] For squarefree coprime a, b: verify c < rad(abc).
    Since rad(n) = n for squarefree n, and abc is squarefree when
    a, b, c=a+b are pairwise coprime and squarefree, we have
    rad(abc) = abc ≥ c. Stronger: c < rad(abc) always. -/
```

## Source Excerpt

```lean
def squarefree_abc_check (bound : Nat) : Bool :=
  go 2 2 ((bound + 1) * (bound + 1))
where
  go (a b fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if a > bound then true
    else if b > bound then go (a + 1) 2 (fuel - 1)
    else
      let g := Nat.gcd a b
      let ok := if g == 1 && is_squarefree a && is_squarefree b then
        let c := a + b
        let r := radical (a * b * c)
        -- For squarefree coprime triples: c < rad(abc)
        r > 0 && c <= r  -- c ≤ rad(abc) (equality rare)
      else true  -- skip non-squarefree or non-coprime
      ok && go a (b + 1) (fuel - 1)
  termination_by fuel
```

---
{
  "projection_kind": "taulib_declaration",
  "title": "no_comprehension",
  "permalink": "/verify/taulib/docs/book-i-sets-cantor-refutation/no-comprehension/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.CantorRefutation`.",
  "declaration_id": "TauLib.BookI.Sets.CantorRefutation::no_comprehension",
  "declaration_slug": "no-comprehension",
  "kind": "theorem",
  "name": "no_comprehension",
  "module_name": "TauLib.BookI.Sets.CantorRefutation",
  "module_url": "/verify/taulib/docs/book-i-sets-cantor-refutation/",
  "source_line_start": 87,
  "source_line_end": 95,
  "registry_ids": [
    "I.P35"
  ],
  "related_registry_items": [
    {
      "id": "I.P35",
      "title": "No Unrestricted Comprehension",
      "url": "/registry/object/I.P35/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L87-L95",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.CantorRefutation",
        "url": "/verify/taulib/docs/book-i-sets-cantor-refutation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L87-L95",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Sets.CantorRefutation](/verify/taulib/docs/book-i-sets-cantor-refutation/)
- Source path: [`TauLib/BookI/Sets/CantorRefutation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/CantorRefutation.lean#L87-L95)
- Source range: L87-L95
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.P35` — No Unrestricted Comprehension

## Immediate Comment / Docstring

```lean
/-- [I.P35] No comprehension separator exists in tau-arithmetic.

    Proof: apply Sep to the Russell predicate P(a) = not(a in_tau a).
    For R = Sep(P), the comprehension schema gives a in_tau R iff not(a in_tau a).
    At a = R: R in_tau R iff not(R in_tau R). But R in_tau R holds by reflexivity
    (R | R), so not(R in_tau R) also holds -- contradiction. -/
```

## Source Excerpt

```lean
theorem no_comprehension :
    ¬ exists (Sep : ComprehensionSep),
      forall (P : TauIdx -> Prop) (a : TauIdx),
        tau_mem a (Sep P) <-> P a := by
  intro ⟨Sep, hSep⟩
  let P : TauIdx -> Prop := fun a => ¬ tau_mem a a
  have hR := hSep P (Sep P)
  have hmem : tau_mem (Sep P) (Sep P) := tau_mem_refl (Sep P)
  exact (hR.mp hmem) hmem
```
